## Kubernetes Deployment

A Minikube Kubernetes cluster was used for orchestration. The application was deployed using a Kubernetes Deployment with 3 replicas and a RollingUpdate strategy.

The application was successfully updated from version 1.0 to version 1.1 using a rolling update.

The deployment was then rolled back from version 1.1 to the previous version 1.0 using:

kubectl rollout undo deployment/devops-deployment

The rollback completed successfully and the deployment returned to version 1.0.

## Kubernetes Service

A NodePort service exposed the application on port 8000 inside the cluster. The application was successfully accessed through the Minikube service tunnel.

Application response:

DevOps Lab 2 - Kubernetes Deployment is Working!

## Scaling Experiment

The deployment was scaled from 3 replicas to 5 replicas using:

kubectl scale deployment devops-deployment --replicas=5

The scaling operation completed successfully.

Final result:

- Desired replicas: 5
- Ready replicas: 5
- Available replicas: 5
- Running pods: 5
- Pod restarts: 0

This demonstrates that Kubernetes can horizontally scale the application by increasing the number of running replicas.

## Observations

1. Docker provided isolated and reproducible application containers.
2. Docker Compose simplified running the container as a service.
3. Kubernetes Deployment maintained the desired number of application replicas.
4. RollingUpdate allowed the application image to be updated from version 1.0 to 1.1 without manually recreating the deployment.
5. Kubernetes rollback successfully restored the deployment from version 1.1 to version 1.0.
6. Kubernetes scaling increased the application replicas from 3 to 5 successfully.
7. The Kubernetes Service provided access to the deployed application.
8. ConfigMap was used to provide the application message through an environment variable.
