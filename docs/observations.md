# Observations

## Environment Setup

Ubuntu 24.04.4 LTS was successfully installed and configured using WSL2.

## Git

Git version 2.43.0 was installed and configured with the GitHub user identity.

## Java

OpenJDK 21 was installed as the Java runtime required by Jenkins.

## Jenkins

Jenkins 2.568.2 was successfully installed and configured as a system service.

## Application

A Python HTTP application was created and tested locally.

## Testing

The application test completed successfully:

    Ran 1 test in 0.000s
    OK

## CI/CD Pipeline

A Jenkins declarative pipeline will be used to automate:

    Build → Test → Deploy

## Deployment

The deployment stage will automatically deploy the application after successful testing.

## Jenkins CI/CD Execution

Jenkins job `devops-lab-1` was configured to retrieve the Jenkinsfile from the GitHub repository.

### Pipeline Stages

The pipeline successfully executed the following stages:

1. Checkout SCM
2. Build
3. Test
4. Deploy

### Build Result

Jenkins Build #1 completed successfully with:

`Finished: SUCCESS`

The deployment stage copied the application to:

`/tmp/devops-lab-1-deployed`

The pipeline demonstrated an automated Build -> Test -> Deploy workflow using Jenkins and GitHub.
