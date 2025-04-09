# 🚀 Kubernetes Day 5 - Scaling, Requests & Limits, and Metrics

## 📚 Topics Covered

- Kubernetes Requests and Limits
- Importance of Resource Management
- Installing Metrics Server
- Demo: Requests and Limits in Action
- Scaling in Kubernetes
- Horizontal vs Vertical Scaling
- HPA (Horizontal Pod Autoscaler) vs VPA (Vertical Pod Autoscaler)
- Cluster Autoscaling vs Node Auto-Provisioning
- Simulated Load and HPA Demo

---

## ⚙️ Kubernetes Requests and Limits

### 🧠 Why Do We Need Them?
- **Requests**: Minimum guaranteed resources a pod needs.
- **Limits**: Maximum resources a pod can consume.
- Prevents resource starvation and ensures fair scheduling.

### 💻 Example Manifest:

```yaml
resources:
  requests:
    memory: "64Mi"
    cpu: "250m"
  limits:
    memory: "128Mi"
    cpu: "500m"
```

---

## 📈 Installing Metrics Server

### 🔧 Commands to Install:

```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

### 🧪 Verify Installation:

```bash
kubectl top nodes
kubectl top pods
```

---

## 🔬 Demo: Requests and Limits

### 🛠️ Deploy a Pod With Limits:

```bash
kubectl run test-pod --image=nginx --requests=cpu=100m,memory=64Mi --limits=cpu=200m,memory=128Mi
```

### 🧪 Check Resources:

```bash
kubectl describe pod test-pod
kubectl top pod test-pod
```

---

## 📈 Scaling in Kubernetes

### ➕ Horizontal Scaling (More Pods)
### ⬆️ Vertical Scaling (More CPU/Memory per Pod)

---

## ⚖️ HPA vs VPA

| Feature | HPA | VPA |
|--------|-----|-----|
| Scales Pods | ✅ | ❌ |
| Adjusts Pod Size | ❌ | ✅ |
| Metrics Used | CPU/Memory/Custom | CPU/Memory |
| Use Case | Dynamic Load | Stable Workloads |

---

## 🔄 Cluster Autoscaling vs Node Auto-Provisioning

- **Cluster Autoscaler**: Adjusts number of nodes based on pod demand.
- **Node Auto-Provisioning**: Automatically adds node types (machine families).

---

## 🚀 Demo: HPA with Load Simulation

### 📦 Create Deployment:

```bash
kubectl create deployment cpu-stress --image=busybox -- /bin/sh -c "while true; do :; done"
```

### 📈 Expose as a service:

```bash
kubectl expose deployment cpu-stress --port=80 --target-port=80 --type=ClusterIP
```

### 📉 Apply HPA:

```bash
kubectl autoscale deployment cpu-stress --cpu-percent=50 --min=1 --max=5
```

### 🔥 Simulate Load (in a separate shell):

```bash
kubectl run -i --tty load-generator --image=busybox /bin/sh
# Inside shell:
while true; do wget -q -O- http://cpu-stress; done
```

### 📊 Monitor:

```bash
kubectl get hpa
kubectl top pods
```

---

## ✅ Conclusion

I learned how to:
- Manage pod resources using requests and limits.
- Install and use the metrics server.
- Scale your workloads horizontally using HPA.
- Compare horizontal and vertical scaling strategies.
