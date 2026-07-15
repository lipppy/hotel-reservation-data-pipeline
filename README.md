# hotel-reservation-data-pipeline

## Overview

This repository contains a small hotel reservation data pipeline developed as part of a one-week Software Development internship project.

The project demonstrates how data can move between different systems and formats using Python. It starts with basic file operations and gradually introduces CSV and JSON processing, MySQL, Docker, REST API integration, data transformation, validation, and export.

The final application processes hotel reservation data through the following pipeline (see [PROJECT.md](PROJECT.md) for the full breakdown):

```
   Apaleo REST API
          ↓
   JSON file (raw response)
          ↓
   CSV file (fields we need)
          ↓
        MySQL
          ↓
  Query by hotel + date range
          ↓
   JSON response → Dashboard
```

The main goal of the project is to provide practical experience with a simplified version of a real-world software integration workflow.


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


## Git Basics

Git tracks changes in the project and allows you to return to an earlier
version if something goes wrong.

### Clone the repository (first time only)

``` bash
git clone <repo-url>
cd hotel-reservation-data-pipeline
```

Use your repository URL from GitHub (HTTPS or SSH).

### Check the current state

``` bash
git status
```

Shows changed, new, and staged files.

### Get the latest changes

``` bash
git fetch
```

Downloads remote updates (branches and commits) without modifying your
working branch.

``` bash
git pull
```

Fetches and merges the latest changes from the remote repository into
your current branch.

### Review your changes

``` bash
git diff
```

Shows what has changed since the last commit.

### Stage changes

``` bash
git add .
```

Prepares all current changes for the next commit.

### Create a commit

``` bash
git commit -m "Add CSV import"
```

Saves a snapshot of the staged changes. Use a short message describing
what you changed.

### Push changes to GitHub

``` bash
git push
```

Uploads commits from your current branch to GitHub.

### Recommended workflow (simple, no feature branch)

``` text
git clone <repo-url>    (first time only)
    ↓
cd hotel-reservation-data-pipeline
    ↓
git pull
    ↓
make some code changes
    ↓
git status
    ↓
git diff
    ↓
git add .
    ↓
git commit -m "Describe the change"
    ↓
git push
```

This is the fastest flow for small learning projects where one person is
working directly on the main branch.

### Alternative workflow (with feature branches)

Use this when collaborating with others or when changes are larger.

Create and switch to a feature branch:

``` bash
git checkout -b feature/short-description
```

Push branch to GitHub (first push):

``` bash
git push -u origin feature/short-description
```

Then open a Pull Request and merge after review.

If Git reports a conflict, rejects a command, or you are unsure what to
do, stop and ask for help instead of trying random commands.


## Docker Basics

Docker runs applications in containers so your local machine setup is less important.

### Start containers

``` bash
docker compose up -d
```

Builds images if needed and starts services in the background.

### Check running services

``` bash
docker compose ps
```

Shows which services are running and on which ports.

### See logs

``` bash
docker compose logs -f
```

Shows live output from containers. Press `Ctrl+C` to stop viewing logs.

### Open a shell inside a container

``` bash
docker compose exec <service_name> /bin/bash
```

If bash is not available in the image, use:

``` bash
docker compose exec <service_name> /bin/sh
```

After entering the container, you can run app commands, for example:

``` bash
python your_file.py
```

### Run a one-off command

``` bash
docker compose run --rm <service_name> python your_file.py
```

Runs a command in a temporary container and removes it after exit.

### Stop containers

``` bash
docker compose down
```

Stops and removes containers, networks, and default compose resources.

### Recommended Workflow

``` text
docker compose up -d
    ↓
docker compose ps
    ↓
docker compose exec <service_name> /bin/bash
    ↓
python your_file.py
    ↓
docker compose down
```

If a container does not start, first run `docker compose logs -f` and check the first error line.
