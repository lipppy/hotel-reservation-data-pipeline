# hotel-reservation-data-pipeline

## Overview

This repository contains a small hotel reservation data pipeline developed as part of a one-week Software Development internship project.

The project demonstrates how data can move between different systems and formats using Python. It starts with basic file operations and gradually introduces CSV and JSON processing, PostgreSQL, Docker, REST API integration, data transformation, validation, and export.

The final application processes hotel reservation data through the following pipeline:

```
CSV / JSON / REST API
          ↓
        Python
          ↓
 Validation & Transformation
          ↓
      PostgreSQL
          ↓
     CSV / JSON Export
          ↓
      Dashboard
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

Uploads your commits to the remote repository.

### Recommended Workflow

``` text
git fetch
    ↓
git pull
    ↓
make changes
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

If Git reports a conflict, rejects a command, or you are unsure what to
do, stop and ask for help instead of trying random commands.
