# Kubernetes - Day 1 Learning

## Kubernetes Replica Set

### **Editing Replica Set**
To edit an existing Replica Set:
```sh
kubectl edit rs/nginx-rs
```

### **Scaling a Replica Set**
To scale the number of replicas to 10:
```sh
kubectl scale --replicas=10 rs/nginx-rs
```

### **Deleting a Replica Controller**
To delete a replication controller:
```sh
kubectl delete rc/nginx-rc
```

### **Explaining Kubernetes Components**
To get details about the Replica Set:
```sh
kubectl explain rs
```

To describe a specific pod:
```sh
kubectl describe pod nginx-rc-r89kf
```

---

## Kubernetes Update Deployment

### **Updating Deployment Image**
To update the image of a deployment:
```sh
kubectl set image deploy/nginx-deploy nginx=nginx:1.9.1
```

### **Checking Rollout History**
To check the deployment rollout history:
```sh
kubectl rollout history deploy/nginx-deploy
```

### **Undoing a Deployment Rollout**
To rollback to the previous deployment version:
```sh
kubectl rollout undo deploy/nginx-deploy
```

---

## Creating a Basic Deployment using Command Line
To create a deployment and save it as a YAML file:
```sh
kubectl create deploy deploy/nginx-new --image=nginx --dry-run=client -o yaml > deploy.yaml
```

---

## Summary
- Learned how to work with Replica Sets (editing, scaling, deleting, and describing them).
- Updated and managed deployments using:
  ```sh
  kubectl set image
  kubectl rollout history
  kubectl rollout undo
  ```
- Created a basic Kubernetes deployment using:
  ```sh
  kubectl create deploy
  ```
  with YAML generation.

This marks my **Day 1** learning of Kubernetes. More to come! 🚀

