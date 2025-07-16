# 🐍🚀 fastapi-k8s-stateful

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)  
[![FastAPI](https://img.shields.io/badge/FastAPI-⚡️-green)](https://fastapi.tiangolo.com/)  
[![Docker](https://img.shields.io/badge/docker-📦-blue)](https://www.docker.com/)  
[![Kubernetes](https://img.shields.io/badge/kubernetes-☸️-blue)](https://kubernetes.io/)  
[![Minikube](https://img.shields.io/badge/minikube-🔧-yellow)](https://minikube.sigs.k8s.io/)

> Hands-on guide to deploy a **stateful** FastAPI service with **persistent storage** on a local Kubernetes cluster (Minikube).

---

## 📚 Table of Contents

1. [Demo Preview](#-demo-preview)  
2. [Prerequisites](#-prerequisites)  
3. [Quick Start](#-quick-start)  
4. [Step-by-Step Guide](#-step%E2%80%91by%E2%80%91step-guide)  
   - 4.1 [Create & Test Your FastAPI App](#41-create--test-your-fastapi-app)  
   - 4.2 [Containerize with Docker](#42-containerize-with-docker)  
   - 4.3 [Provision PVC & Headless Service](#43-provision-pvc--headless-service)  
   - 4.4 [Deploy StatefulSet & NodePort Service](#44-deploy-statefulset--nodeport-service)  
   - 4.5 [Smoke-Test & Scale](#45-smoke%E2%80%91test--scale)  
   - 4.6 [Clean Up](#46-clean-up)  
5. [Common Pitfalls](#-common-pitfalls)  
6. [Next Steps](#-next-steps)

---

## 👀 Demo Preview

![Stateful Workflow](./assets/stateful-demo.gif)  
_Stateful pods each with their own PVC, serving `/save` & `/read`._

---

## ⚙️ Prerequisites

- **Python 3.11+**  
- **Docker Desktop** (WSL2 on Windows) or Docker CE on Linux/macOS  
- **Minikube v1.36+**  
- **kubectl** (match your Minikube version)  
- A code editor (VS Code, PyCharm…)  
- Basic CLI skills (bash / PowerShell)

---

## 🚀 Quick Start

```bash
# 1. Clone
git clone https://github.com/<you>/fastapi-k8s-stateful.git
cd fastapi-k8s-stateful

# 2. Build & Push to Minikube’s Docker
minikube start --driver=docker
minikube docker-env --shell bash | source /dev/stdin
docker build -t fastapi-stateful .

# 3. Apply Kubernetes Manifests
kubectl apply -f pvc.yaml
kubectl apply -f headless-service.yaml
kubectl apply -f statefulset.yaml
kubectl apply -f nodeport-service.yaml

# 4. Verify
kubectl get pvc,pods,svc

# 5. Access & Test
URL=$(minikube service fastapi-access --url)
curl -X POST $URL/save -d "hello from pod"
curl $URL/read

# 6. Cleanup
kubectl delete svc,statefulset,pvc --all
minikube stop
