# Kubernetes Learning - Day 4

## **Taints, Tolerations, and Node Affinity in Kubernetes**

This document covers key Kubernetes concepts related to **Taints, Tolerations, Labels, Selectors, and Node Affinity**, along with essential commands for practical implementation.

---

## **1️⃣ Taints in Kubernetes**
Taints are used to repel pods from scheduling on specific nodes.

### **Commands:**
```sh
kubectl taint nodes <node-name> key=value:NoSchedule
kubectl describe node <node-name> | grep Taint
kubectl taint nodes <node-name> key=value:NoSchedule-
```

---

## **2️⃣ Tolerations in Kubernetes**
Tolerations allow pods to schedule on nodes with matching taints.

### **Example YAML:**
```yaml
tolerations:
  - key: "key"
    operator: "Equal"
    value: "value"
    effect: "NoSchedule"
```

### **Apply and Check Deployment:**
```sh
kubectl apply -f pod.yaml
kubectl get pods -o wide
```

---

## **3️⃣ Labels and Selectors vs. Taints and Tolerations**
Labels and Selectors are used to group and filter Kubernetes objects, while Taints and Tolerations control scheduling behavior.

### **Commands:**
```sh
kubectl label nodes <node-name> key=value
kubectl get nodes --show-labels
kubectl get pods --selector key=value
kubectl get nodes -l key=value
```

---

## **4️⃣ Demo: Taints and Tolerations in Action**
### **Commands:**
```sh
kubectl taint nodes <node-name> key=value:NoSchedule
kubectl apply -f pod-with-tolerations.yaml
kubectl get pods -o wide
kubectl describe pod <pod-name>
```

---

## **5️⃣ Node Affinity in Kubernetes**
Node Affinity helps in scheduling pods on specific nodes based on labels.

### **Example YAML:**
```yaml
affinity:
  nodeAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      nodeSelectorTerms:
      - matchExpressions:
        - key: "key"
          operator: "In"
          values:
          - "value"
```

### **Apply and Check Deployment:**
```sh
kubectl apply -f pod-affinity.yaml
kubectl get pods -o wide
```

---

## **6️⃣ Different Types of Properties in Node Affinity**
### **Commands:**
```sh
kubectl label nodes <node-name> key=value
kubectl get nodes --show-labels
kubectl describe node <node-name>
```

---

## **7️⃣ Demo: Setting Up Node Affinity**
### **Commands:**
```sh
kubectl apply -f pod-with-node-affinity.yaml
kubectl get pods -o wide
kubectl describe pod <pod-name>
kubectl get nodes -l key=value
```

---

## 🎯 **Summary**

🔹 Explored **Taints and Tolerations** to control pod scheduling ⚙️  
🔹 Used **Labels and Selectors** for resource grouping 🏷️  
🔹 Implemented **Node Affinity** for intelligent pod placement 🌍  
🔹 Ran `kubectl` commands to manage and debug configurations 🛠️  

---

👨‍💻 **Author:** Prashant Lalwani  
📅 **Day 4 of Kubernetes Learning** 🎯

