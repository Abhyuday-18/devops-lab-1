# Lab 2 – Containerization & Kubernetes Orchestration

## Objective

To containerize an application using Docker, manage it using Docker Compose, and deploy, scale, and update the application using Kubernetes on a Minikube cluster.

## 1. Docker Containerization

The application was containerized using a Dockerfile based on Python 3.12 Slim.

Docker image created:

    devops-lab-1:1.0

Command:

    docker build -t devops-lab-1:1.0 .

The Docker container was started using:

    docker run -d --name devops-lab-1-container -p 8000:8000 devops-lab-1:1.0

The application was verified using:

    curl http://localhost:8000

The application responded successfully.

## 2. Docker Compose

Docker Compose was verified using:

    docker compose version

A docker-compose.yml file was created to build and run the application.

The Compose application was started using:

    docker compose up -d --build

The running container was verified using:

    docker compose ps

The application was tested using:

    curl http://localhost:8001

Output:

    DevOps Lab 2 - Docker Compose is Working!

After testing, the Compose resources were stopped using:

    docker compose down

## 3. Kubernetes Cluster

Minikube was started using the Docker driver:

    minikube start --driver=docker

The cluster status was verified using:

    minikube status

The Minikube cluster was running successfully.

## 4. Docker Image in Minikube

The Docker image was loaded into Minikube using:

    minikube image load devops-lab-1:1.0

The application was then updated to use a ConfigMap-provided environment variable.

A new image version was built:

    docker build -t devops-lab-1:1.1 .

The updated image was loaded into Minikube:

    minikube image load devops-lab-1:1.1

## 5. Kubernetes Configuration

Three Kubernetes resources were created:

- ConfigMap
- Deployment
- Service

### ConfigMap

The ConfigMap provides the application message through the MESSAGE environment variable.

    MESSAGE = DevOps Lab 2 - Kubernetes Deployment is Working!

### Deployment

The Deployment uses:

- 3 replicas
- RollingUpdate strategy
- maxUnavailable: 1
- maxSurge: 1
- Image: devops-lab-1:1.1

### Service

A NodePort Service exposes the application on port 8000.

## 6. Kubernetes Deployment

The Kubernetes manifests were applied using:

    kubectl apply -f k8s/

The Deployment was verified using:

    kubectl get deployment devops-deployment

The final Deployment showed:

    3/3 READY
    3 UP-TO-DATE
    3 AVAILABLE

The Pods were verified using:

    kubectl get pods

All three Pods were running successfully.

## 7. Scaling

The Deployment was temporarily scaled from 3 to 5 replicas using:

    kubectl scale deployment devops-deployment --replicas=5

The scaling operation was verified using:

    kubectl get deployment
    kubectl get pods

Five Pods were successfully created and reached the Running state.

The Deployment was subsequently returned to the final manifest-defined state of 3 replicas.

## 8. Rolling Update

The application was updated from image version 1.0 to version 1.1.

The Deployment image was changed to:

    devops-lab-1:1.1

The updated Deployment was applied using:

    kubectl apply -f k8s/deployment.yaml

The rollout was verified using:

    kubectl rollout status deployment/devops-deployment

Result:

    deployment "devops-deployment" successfully rolled out

## 9. Application Verification

The Kubernetes Service was exposed using:

    minikube service devops-service --url

The application was tested through the generated Service URL.

Final response:

    DevOps Lab 2 - Kubernetes Deployment is Working!

This confirmed that:

1. The Docker image was deployed successfully.
2. Kubernetes created and managed the application Pods.
3. The Service routed traffic to the Pods.
4. The ConfigMap value was passed to the application through an environment variable.
5. The rolling update to image version 1.1 completed successfully.

## Conclusion

The containerization and Kubernetes orchestration workflow was successfully implemented using Docker, Docker Compose, Minikube, and kubectl. The application was containerized, executed with Docker Compose, deployed with multiple Kubernetes replicas, scaled, updated using a RollingUpdate strategy, and exposed through a Kubernetes Service.
