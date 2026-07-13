"""Lightweight Apaleo API client.

This client reads ``APALEO_CLIENT_ID`` and ``APALEO_CLIENT_SECRET`` from the
environment, typically loaded from a local ``.env`` file.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any

import requests
from dotenv import load_dotenv

DEFAULT_API_BASE_URL = "https://api.apaleo.com"
DEFAULT_TOKEN_URL = "https://identity.apaleo.com/connect/token"


@dataclass(slots=True)
class ApaleoCredentials:
    """Apaleo client credentials loaded from environment variables."""

    client_id: str
    client_secret: str


class ApaleoClient:
    """Minimal wrapper around Apaleo authentication and HTTP requests."""

    def __init__(
        self,
        client_id: str | None = None,
        client_secret: str | None = None,
        *,
        api_base_url: str = DEFAULT_API_BASE_URL,
        token_url: str = DEFAULT_TOKEN_URL,
        scope: str | None = None,
        timeout: int = 30,
        session: requests.Session | None = None,
    ) -> None:
        load_dotenv()

        credentials = self._resolve_credentials(client_id, client_secret)

        self.client_id = credentials.client_id
        self.client_secret = credentials.client_secret
        self.api_base_url = api_base_url.rstrip("/")
        self.token_url = token_url
        self.scope = scope
        self.timeout = timeout
        self.session = session or requests.Session()
        self._access_token: str | None = None

    @staticmethod
    def _resolve_credentials(
        client_id: str | None,
        client_secret: str | None,
    ) -> ApaleoCredentials:
        resolved_client_id = client_id or os.getenv("APALEO_CLIENT_ID")
        resolved_client_secret = client_secret or os.getenv("APALEO_CLIENT_SECRET")

        if not resolved_client_id or not resolved_client_secret:
            raise ValueError(
                "Missing Apaleo credentials. Set APALEO_CLIENT_ID and "
                "APALEO_CLIENT_SECRET in your environment or .env file."
            )

        return ApaleoCredentials(
            client_id=resolved_client_id,
            client_secret=resolved_client_secret,
        )

    def get_access_token(self) -> str:
        """Fetch and cache an access token using the client credentials flow."""

        if self._access_token:
            return self._access_token

        data: dict[str, Any] = {"grant_type": "client_credentials"}
        if self.scope:
            data["scope"] = self.scope

        response = self.session.post(
            self.token_url,
            data=data,
            auth=(self.client_id, self.client_secret),
            timeout=self.timeout,
        )
        if not response.ok:
            raise requests.exceptions.HTTPError(
                f"{response.status_code} error requesting access token: {response.text}",
                response=response,
            )

        token_payload = response.json()
        self._access_token = token_payload["access_token"]
        return self._access_token

    def request(self, method: str, path: str, **kwargs: Any) -> requests.Response:
        """Send an authenticated request to the Apaleo API."""

        headers = kwargs.pop("headers", {})
        headers["Authorization"] = f"Bearer {self.get_access_token()}"

        params = kwargs.pop("params", None)

        url = f"{self.api_base_url}/{path.lstrip('/')}"
        response = self.session.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            timeout=kwargs.pop("timeout", self.timeout),
            **kwargs,
        )
        response.raise_for_status()
        return response

    def get(self, path: str, **kwargs: Any) -> requests.Response:
        """Convenience wrapper for GET requests."""

        return self.request("GET", path, **kwargs)
