# Day 8: Kubernetes Certificate Authentication & API Server Communication

Today’s focus is on understanding **how Kubernetes uses certificates for secure communication**, especially between the master (control plane) components and worker nodes, and how we can add **an external user** securely to the Kubernetes cluster.

---

## 🔐 Secure Communication in Kubernetes

Kubernetes uses **TLS certificates** and **private keys** for authentication and secure communication between its components:

- The **kube-apiserver** acts as:
  - A **server** to external clients/users.
  - A **client** to internal components like **kubelet**, **etcd**, etc.

Refer to the diagrams:

1. The first diagram demonstrates the direction of secure communication:
   - The API server communicates with multiple kubelets running on Worker Node A, B, and C.

2. The second diagram breaks down the authentication infrastructure:
   - Every major component (API server, kube-scheduler, etc.) uses a **certificate** and **private key**.
   - Users also authenticate using certificates.

---

## 👤 Adding an External User (e.g., `prashant`)

Here’s a step-by-step walkthrough for adding an external user to a Kubernetes cluster using certificate signing:

### 1. Generate Private Key
```bash
openssl genrsa -out prashant.key 2048
```
This generates a 2048-bit RSA private key for the user `prashant`.

### 2. Create CSR (Certificate Signing Request)
```bash
openssl req -new -key prashant.key -out prashant.csr -subj "/CN=prashant"
```
The `CN` (Common Name) here becomes the user identity in Kubernetes.

### 3. Base64 Encode the CSR for Kubernetes
You’ll need to base64 encode the CSR content to use it in a manifest:
```bash
cat prashant.csr | base64 | tr -d "\n"
```

### 4. Create `csr.yaml`
```yaml
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: prashant
spec:
  request: <base64-encoded-csr>
  signerName: kubernetes.io/kube-apiserver-client
  expirationSeconds: 86400  # Optional, here it's 1 day
  usages:
    - client auth
  groups:
    - system:authenticated
```

### 5. Apply the CSR
```bash
kubectl apply -f csr.yaml
```

### 6. Approve the Certificate Request
```bash
kubectl certificate approve prashant
```

### 7. Extract the Issued Certificate
```bash
kubectl get csr prashant -o yaml > issuecert.yaml
```
From this YAML, extract the base64-encoded certificate and decode it:
```bash
echo "<certificate-from-status-field>" | base64 -d > prashant.crt
```

---

## 🔄 What Just Happened?
- You created a **TLS client certificate** for an external user.
- The Kubernetes **API server** recognized and authenticated this certificate via **CSR approval**.
- The user can now interact securely with the Kubernetes cluster using a `kubeconfig` that includes:
  - `prashant.crt`
  - `prashant.key`

---

## 🔎 Insights & Takeaways

- 🔐 **Every communication in Kubernetes is secured via certificates**.
- 📌 The **kube-apiserver is central** to all communication—it authenticates requests from users, talks to the kubelet, ETCD, and other components.
- 🧩 **CSR approval** is a manual trust step, ensuring only verified identities get access.
- 📁 The user’s certificate can be plugged into `kubeconfig` for authenticated access.

---

This wraps up Day 8! We now have a clearer understanding of TLS-based communication in Kubernetes and how to securely add users to the cluster.

Stay tuned for Day 9! 🚀

