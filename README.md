# 🚀 Kubernetes FastAPI Labs

Two hands-on labs to master how to containerize FastAPI apps and run them on a local Kubernetes cluster powered by Minikube.

- **Lab 1:** Deploy & manage a **stateless** FastAPI web-service  
- **Lab 2:** Deploy & manage a **stateful** FastAPI service with persistent storage

---

## 📋 Table of Contents

1. [Demo Preview](#demo-preview)  
2. [Prerequisites](#prerequisites)  
3. [Quick Start](#quick-start)  
4. [Lab 1: Stateless FastAPI App](#lab-1-stateless-fastapi-app)  
   - 4.1 [Create & Test Locally](#41-create--test-locally)  
   - 4.2 [Dockerize](#42-dockerize)  
   - 4.3 [Run in Minikube](#43-run-in-minikube)  
   - 4.4 [Kubernetes Deployment & Service](#44-kubernetes-deployment--service)  
   - 4.5 [Scale & Monitor](#45-scale--monitor)  
   - 4.6 [Clean Up](#46-clean-up)  
5. [Lab 2: Stateful FastAPI App](#lab-2-stateful-fastapi-app)  
   - 5.1 [Create & Test Locally](#51-create--test-locally)  
   - 5.2 [Dockerize](#52-dockerize)  
   - 5.3 [PVC & Headless Service](#53-pvc--headless-service)  
   - 5.4 [StatefulSet & NodePort Service](#54-statefulset--nodeport-service)  
   - 5.5 [Smoke-Test & Scale](#55-smoke-test--scale)  
   - 5.6 [Clean Up](#56-clean-up)  
6. [🛠 Common Pitfalls](#-common-pitfalls)  
7. [🔮 Next Steps](#-next-steps)  

---

## Demo Preview

![Stateless Lab](./assets/lab1-demo.png)  
*Stateless FastAPI responding through NodePort*

![Stateful Lab](./assets/lab2-demo.png)  
*Stateful FastAPI persisting data via PVC*

---

## Prerequisites

| Tool / Setup                     | Why?                                              |
| -------------------------------- | ------------------------------------------------- |
| **Python 3.8+**                  | Local FastAPI dev & requirements generation      |
| **Docker**                       | Build & run container images                     |
| **Minikube**                     | Local Kubernetes cluster                         |
| **kubectl**                      | CLI for interacting with Kubernetes              |
| **VS Code / Any editor**         | Edit code & YAML                                 |
| **Basic CLI skills**             | Navigate filesystem & run commands               |
| **Internet**                     | Pull Docker base images & Python packages        |

💡 **OS**: Linux, macOS or Windows 10/11 (with WSL2)

---

## Quick Start

```bash
# Clone repo
git clone https://github.com/<your-user>/fastapi-k8s-labs.git
cd fastapi-k8s-labs

# Lab 1 ▶️
cd fastapi-k8s-lab
# follow steps in README under "Lab 1"

# Lab 2 ▶️
cd ../fastapi-stateful-k8s
# follow steps in README under "Lab 2"
