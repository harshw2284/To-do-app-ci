# Task Manager API & Web Application  [![Continuous Integration (CI)](https://github.com/harshw2284/my-app-ci/actions/workflows/ci.yml/badge.svg)](https://github.com/harshw2284/my-app-ci/actions/workflows/ci.yml)

A lightweight, containerized Python Flask To-Do application built for continuous integration (CI/CD) testing, Docker deployments, and quick hosting.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-3.0.3-green)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)

## Features

* **Modern Interface:** Dark-mode responsive UI designed with CSS variables.
* **Core Task Management:** Add new tasks, toggle completion states, and remove items.
* **CI/CD Ready:** Exposes port `5000` and binds to `0.0.0.0` for container networking and health checks.
* **Zero Database Overhead:** Uses an in-memory data store for lightweight, fast pipeline test executions.

## Tech Stack


| Layer      | Technology                           |
|------------|--------------------------------------|
| Frontend   | HTML5, Modern CSS                    |
| Backend    | Python, Flask                        |
| Containers | Docker                               |

## Directory Structure

```text
├── app.py              # Flask server and routing logic
├── requirements.txt    # Application dependencies
├── Dockerfile          # Multi-stage production Dockerfile
├── .dockerignore       # Docker build exclusion rules
└── templates/
    └── index.html      # Frontend HTML layout
