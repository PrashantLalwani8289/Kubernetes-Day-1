# 🚀 Day 2: Learning Kubernetes with Kind, Deployments & NodePort Services

Welcome to **Day 2** of my Kubernetes learning journey! 🎯 Today, I explored how to:
- Set up a Kubernetes cluster using **Kind** 🏗️
- Deploy an **nginx** application with a **Deployment** 📦
- Expose the application using a **NodePort Service** 🌐
- Use `kubectl` commands to interact with the cluster 🔍

---

## 🛠️ Setting Up the Cluster

### **1️⃣ Creating a Kind Cluster**
I used the following `kind.yaml` file to create a multi-node Kubernetes cluster with **one control-plane** and **two worker nodes**:

```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
  - role: control-plane
    extraPortMappings:
      - containerPort: 30007
        hostPort: 30007
  - role: worker
  - role: worker
```

⏳ **Command to create the cluster:**
```sh
kind create cluster --config kind.yaml --name cluster
```

---

## 🏗️ Deploying an Nginx Application

### **2️⃣ Creating a Deployment**
I deployed an **nginx** pod using the following `deployment.yml` file:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deploy
  labels:
    env: demo
spec:
  replicas: 3
  selector:
    matchLabels:
      env: demo
  template:
    metadata:
      name: nginx
      labels:
        env: demo
    spec:
      containers:
        - image: nginx
          name: nginx
          ports:
            - containerPort: 80
```

⏳ **Command to deploy nginx:**
```sh
kubectl apply -f deployment.yml
```

✅ **Check if the pods are running:**
```sh
kubectl get pods
```

🔍 **Describe a specific pod:**
```sh
kubectl describe pod nginx-deploy-<POD_ID>
```

---

## 🌐 Exposing the Application using NodePort

### **3️⃣ Creating a NodePort Service**
The following `nodeport.yml` file exposes the **nginx deployment** on port **30007**:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nodeport-service
  labels:
    env: demo
spec:
  type: NodePort
  selector:
    env: demo
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
      nodePort: 30007
```

⏳ **Command to create the NodePort service:**
```sh
kubectl apply -f nodeport.yml
```

✅ **Verify the service is running:**
```sh
kubectl get svc
```

🔍 **Describe the service:**
```sh
kubectl describe svc/nodeport-service
```

🚀 **Access the application in the browser or via curl:**
```sh
curl localhost:30007
```

---

## 🔧 Other Useful Commands

- **Get a specific pod:**
  ```sh
  kubectl get pod nginx-deploy-<POD_ID>
  ```
- **Apply the ReplicaSet file (if needed):**
  ```sh
  kubectl apply -f rc.yaml
  ```
- **Create the NodePort service again (if needed):**
  ```sh
  kubectl create -f nodeport.yml
  ```

---

## 🎯 Summary

🔹 Created a multi-node **Kind** cluster 🏗️  
🔹 Deployed an **nginx** application using a **Deployment** 📦  
🔹 Exposed it via a **NodePort** service 🌐  
🔹 Used `kubectl` commands to manage and debug the cluster 🛠️  

📌 **Next Steps:** Explore Ingress controllers and ConfigMaps in Kubernetes! 🚀

---

👨‍💻 **Author:** Prashant Lalwani  
📅 **Day 2 of Kubernetes Learning** 🎯

