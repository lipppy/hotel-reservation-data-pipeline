# hotel-reservation-data-pipeline


## Minimal WSL setup (Ubuntu)

### Start WSL

From Windows terminal (PowerShell or CMD):

```bash
wsl
```

Optional (specific distro):

```bash
wsl -d Ubuntu
```

### Exit WSL

```bash
exit
```

### Install required tools inside WSL

```bash
sudo apt update

sudo apt install -y \
	git \
	curl \
	wget \
	make \
	jq \
	tree \
	nano \
	vim
```

### Docker for this task

Install Docker and Docker Compose support.

Recommended: Docker Desktop on Windows with WSL integration enabled.

Alternative (inside WSL):

[Docker installation guide](https://docs.docker.com/engine/install/ubuntu/)


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
