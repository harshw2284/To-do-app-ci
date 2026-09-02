# Task Manager API & Web Application  [![Continuous Integration (CI)](https://github.com/harshw2284/my-app-ci/actions/workflows/ci.yml/badge.svg)](https://github.com/harshw2284/my-app-ci/actions/workflows/ci.yml)

A lightweight, containerized Python Flask To-Do application built for continuous integration (CI/CD) testing, Docker deployments, and quick hosting.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-3.0.3-green)
![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-orange.svg)

<img width="1914" height="850" alt="image" src="https://github.com/user-attachments/assets/948f29f0-72c2-4c76-a59b-061d24643bf5" />

## Features

* **Modern Interface:** Dark-mode responsive UI designed with CSS variables.
* **Core Task Management:** Add new tasks, toggle completion states, and remove items.
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
| 2 | Lint | Flake8 | Enforces Python coding standards |
| 3 | SAST | Bandit | scans Python code for security issues |
| 4 | Dependency Test | pip-audit | scan Python environments and dependency files for known security vulnerabilities |
| 5 | Unit Test | Pytest | Verify the application actually works |

## Pipeline Steps

1. Checkout Code

GitHub Actions checks out the latest source code from the repository so that the workflow can work with the project files.

2. Set Up Python

The workflow installs and configures the required Python version for the application.

3. Install Dependencies

The required Python packages and testing/security tools are installed using pip.

4. Flake8 – Linting

Flake8 checks the Python source code for syntax errors, formatting issues, and other code-quality problems.

5. pip-audit – Dependency Security

pip-audit checks the project's Python dependencies for known security vulnerabilities.

6. Bandit – SAST

Bandit performs static application security testing on the Python source code and identifies potentially insecure coding practices.

7. Gitleaks – Secret Scanning

Gitleaks scans the repository for accidentally committed secrets such as API keys, passwords, and access tokens.

8. Pytest – Automated Testing

Pytest executes the project's automated tests to verify that the application behaves as expected.

9. CI Result

If all checks complete successfully, GitHub Actions marks the workflow as successful. If any check fails, the workflow reports a failure so that the issue can be fixed before the code is considered valid.

Trigger

The workflow is automatically triggered when code is pushed to the GitHub repository.

**CI**:

<img width="1370" height="565" alt="image" src="https://github.com/user-attachments/assets/59b4b12c-5c7b-4d95-a53f-91651e4c5f5e" />

---
