# DevOps Lab 1 - Foundations & Continuous Integration

## Objective

This project demonstrates a basic DevOps workflow using Git, GitHub, Jenkins and a Python application.

## Tools Used

- Ubuntu 24.04 LTS
- Git
- GitHub
- Visual Studio Code
- Jenkins
- Python 3

## CI/CD Pipeline

The Jenkins pipeline contains the following stages:

1. Build
2. Test
3. Deploy

### Build

The application is compiled using Python's `compileall` module.

### Test

Automated unit tests are executed using Python's `unittest` framework.

### Deploy

The application is copied to a deployment directory and started automatically by Jenkins.

## Application

The sample application is a simple HTTP server running on port 8000.

## Repository Structure

```text
devops-lab-1/
├── app/
│   ├── app.py
│   └── test_app.py
├── docs/
│   └── screenshots/
├── Jenkinsfile
└── README.md
