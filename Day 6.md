# Kubernetes Learning - Day 6: Probes & Pod Health Monitoring

On Day 6 of my Kubernetes journey, I explored **Probes in Kubernetes** for monitoring and ensuring container health, as well as understanding how Kubernetes handles failed health checks using **taints and tolerations**.

---

## 🌍 Topics Covered

### 1. **Types of Probes**
- **Command Probes (execAction):** Runs a command inside the container.
- **HTTP Probes (httpGet):** Sends an HTTP request to the container.
- **TCP Probes (tcpSocket):** Opens a TCP socket to check if the container is alive.

### 2. **Liveness vs Readiness Probes**
- **Liveness Probe:** Checks if the container should be restarted.
- **Readiness Probe:** Checks if the container is ready to accept traffic.

---

## 💡 Practice Commands & Demos

### ✅ Command-Based Liveness Probe Demo

**Pod Spec:**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: liveness-command-demo
spec:
  containers:
  - name: liveness-demo
    image: busybox
    args:
    - /bin/sh
    - -c
    - "touch /tmp/healthy; sleep 30; rm -f /tmp/healthy; sleep 600"
    livenessProbe:
      exec:
        command:
        - cat
        - /tmp/healthy
      initialDelaySeconds: 5
      periodSeconds: 5
```

**Command to apply:**
```bash
kubectl apply -f liveness-command-demo.yaml
```

---

### ✨ HTTP-Based Liveness & Readiness Probe Demo

**Pod Spec:**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: http-probes-demo
spec:
  containers:
  - name: agnhost-demo
    image: registry.k8s.io/e2e-test-images/agnhost:2.40
    args:
    - "netexec"
    - "--http-port=8080"
    ports:
    - containerPort: 8080
    livenessProbe:
      httpGet:
        path: /healthz
        port: 8080
      initialDelaySeconds: 5
      periodSeconds: 10
    readinessProbe:
      httpGet:
        path: /healthz
        port: 8080
      initialDelaySeconds: 5
      periodSeconds: 10
```

**Command to apply:**
```bash
kubectl apply -f http-probes-demo.yaml
```

---

## 🔴 Bonus Learning: Taints and Tolerations on Failed Health Checks

When a pod continuously fails health probes (liveness or readiness), Kubernetes may **evict or reschedule** the pod by applying node taints like:

```yaml
- key: node.kubernetes.io/unreachable
  operator: Exists
  effect: NoExecute
  tolerationSeconds: 300
```

You can see these tolerations auto-added in the pod description when such failures happen, as shown in the screenshot.

---

## 🎓 Summary
- Implemented liveness checks using command probes.
- Tested readiness and liveness using HTTP probes.
- Observed Kubernetes' self-healing with taints & tolerations.

These probes ensure robust container orchestration by restarting or holding traffic when things go wrong.

---
