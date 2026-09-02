# Task Manager API & Web Application  [![Continuous Integration (CI)](https://github.com/harshw2284/my-app-ci/actions/workflows/ci.yml/badge.svg)](https://github.com/harshw2284/my-app-ci/actions/workflows/ci.yml)

A lightweight, containerized Python Flask To-Do application built for continuous integration (CI/CD) testing, Docker deployments, and quick hosting.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-3.0.3-green)
![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-orange.svg)

<img width="1914" height="850" alt="image" src="https://github.com/user-attachments/assets/948f29f0-72c2-4c76-a59b-061d24643bf5" />

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
├── dockerfile          # Multi-stage production Dockerfile
├── .dockerignore       # Docker build exclusion rules
└── templates/
    └── index.html      # Frontend HTML layout
```

## Security Pipeline 

The CI pipeline enforces **5 sequential security gates** before any code reaches production:

| Gate | Name | Tool | Purpose |
| :---: | :--- | :--- | :--- |
| 1 | Secret Scan | Gitleaks | Scans entire Git history for leaked secrets |
| 2 | Lint | Checkstyle | Enforces Python coding standards |
| 3 | SAST | Bandit | scans Python code for security issues |
| 4 | Dependency Test | pip-audit | scan Python environments and dependency files for known security vulnerabilities |
| 5 | Unit Test | Pytest | Verify the application actually works |

**CI**:

<img width="670" height="581" alt="image" src="https://github.com/user-attachments/assets/52c54b77-054c-4f94-83f9-61b98a486e33" />


