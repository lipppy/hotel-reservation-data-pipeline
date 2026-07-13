COMPOSE = docker compose
SERVICE = python

.PHONY: help up down shell exec bash run py

help:
	@echo "Targets:"
	@echo "  make up                - Build image and start container in background"
	@echo "  make down              - Stop and remove container"
	@echo "  make shell             - Open interactive Python shell"
	@echo "  make exec              - Open Python shell in running container"
	@echo "  make bash              - Open bash in running container"
	@echo "  make run FILE=app.py   - Run a Python file"


up:
	$(COMPOSE) up -d --build

down:
	$(COMPOSE) down

shell:
	$(COMPOSE) run --rm --build $(SERVICE) python

exec:
	$(COMPOSE) exec $(SERVICE) python

bash:
	$(COMPOSE) exec $(SERVICE) /bin/bash

run:
	@if [ -z "$(FILE)" ]; then echo "Usage: make run FILE=path/to/script.py"; exit 1; fi
	$(COMPOSE) run --rm --build $(SERVICE) python $(FILE)
