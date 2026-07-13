# hotel-reservation-data-pipeline

## Local Python via Docker

Simple Python 3.12 environment with the whole project mounted into the container.
Changes in the project folder are immediately visible inside the container via bind mount.

### Requirements

- Docker
- Docker Compose (available as `docker compose`)

### Commands

- `make help` - show available targets
- `make up` - start container in background
- `make shell` - start interactive Python shell
- `make run FILE=path/to/script.py` - run a Python file
- `make down` - stop and remove container
