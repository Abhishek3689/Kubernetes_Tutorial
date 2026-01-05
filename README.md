# Kubernetes Learning Tutorial 🚀

This repository contains **hands-on Kubernetes examples** created for learning core concepts step by step using **Minikube**.

The goal is to understand **how Kubernetes works internally**, not just run commands.

---

## 📌 Prerequisites
- Docker
- Minikube
- kubectl
- Basic YAML knowledge

---

## 🧱 Core Kubernetes Concepts Covered

### 1️⃣ Basic Objects
- Pod
- ReplicaSet
- Deployment
- Service (ClusterIP, NodePort)
- Namespace

### 2️⃣ Configuration Management
- ConfigMap
- Secret
- Environment Variables
- File-based config

### 3️⃣ Storage
- PersistentVolume (PV)
- PersistentVolumeClaim (PVC)
- Storage lifecycle
- hostPath (Minikube)

### 4️⃣ Controllers
- Job
- CronJob
- DaemonSet
- StatefulSet (with MySQL example)

### 5️⃣ Networking
- Service Discovery
- DNS inside cluster
- Pod-to-Pod communication
- Headless Service

---

## 🛠️ Hands-on Examples
- Deploying applications using Deployment
- Scaling pods
- Exposing apps using Services
- Running scheduled tasks with CronJob
- Running MySQL using StatefulSet + PVC
- Debugging CrashLoopBackOff & BackOff errors

---

## 🔍 Debugging Commands (Very Important)
```bash
kubectl get pods
kubectl describe pod <pod-name>
kubectl logs <pod-name>
kubectl exec -it <pod-name> -- bash
