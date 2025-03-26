# Kubernetes Namespaces - Practical Guide

## 🏗️ Day 3 - Kubernetes Namespaces and Service Discovery
Namespaces help organize and manage resources in Kubernetes clusters. Below are practical steps and commands for working with namespaces and deploying services.

### 📌 Creating and Managing Namespaces
```sh
# List all namespaces
kubectl get ns

# Create a new namespace
kubectl create ns demo

# Verify namespace creation
kubectl get ns demo

# Delete a namespace
kubectl delete ns demo
```

### 🚀 Deploying Applications in a Namespace
```sh
# Create a deployment in the 'demo' namespace
kubectl create deploy nginx-demo --image=nginx -n demo

# Scale the deployment to 3 replicas
kubectl scale --replicas=3 deploy/nginx-demo -n demo

# Verify the deployment
kubectl get deploy -n demo
kubectl get pods -n demo -o wide
```

### 🌍 Exposing the Deployment as a Service
```sh
# Expose the deployment as a service
kubectl expose deploy/nginx-demo --name=svc-demo --port=80 -n demo

# List services in the 'demo' namespace
kubectl get svc -n demo
```

### 🔗 Connecting Between Services in Different Namespaces
```sh
# Check the FQDN of a service
kubectl get svc -n demo

# Access service from within a pod
kubectl exec -it <nginx-pod-name> -n demo -- sh
curl svc-demo.demo.svc.cluster.local
exit
```

### 🛠️ Debugging & Troubleshooting
```sh
# Get all resources in a namespace
kubectl get all -n demo

# Get detailed pod info
kubectl describe pod <pod-name> -n demo

# Check logs of a pod
kubectl logs <pod-name> -n demo

# Get DNS resolution details inside a pod
kubectl exec -it <nginx-pod-name> -n demo -- cat /etc/resolv.conf
```

### 🔥 Cleaning Up
```sh
# Delete deployment and service
kubectl delete deploy nginx-demo -n demo
kubectl delete svc svc-demo -n demo

# Delete namespace (removes all resources inside)
kubectl delete ns demo
```

## ✅ Conclusion
This practical guide covers the basics of working with Kubernetes namespaces, deploying applications, exposing services, and troubleshooting. These commands will help you efficiently manage isolated environments within your cluster. 🚀

