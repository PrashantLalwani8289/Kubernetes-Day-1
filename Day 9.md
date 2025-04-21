# Kubernetes Learning - Day 9

## 🧠 Focus: RBAC (Role-Based Access Control) and User Access Verification

### ✅ Objective:
Learn how to create Kubernetes roles and role bindings, manage user authentication using client certificates, and verify access control using `kubectl auth can-i`.

---

## 🔐 Step 1: Check Current Access Permissions

```bash
kubectl auth can-i get pods
kubectl auth whoami
```

---

## 👤 Step 2: Simulate Access as Another User

```bash
kubectl auth can-i get pods --as prashant
```

---

## 📜 Step 3: Create a Role

Define a role that grants permission to read pods:

```yaml
# Role/role.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: default
  name: pod-reader
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "watch", "list"]
```

Apply the role:

```bash
kubectl apply -f Role/role.yaml
```

Verify:

```bash
kubectl get roles
kubectl describe role pod-reader
```

---

## 🔗 Step 4: Bind Role to a User

```yaml
# Role/binding.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: read-pods
  namespace: default
subjects:
- kind: User
  name: prashant
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```

Apply the binding:

```bash
kubectl apply -f Role/binding.yaml
```

Verify:

```bash
kubectl get rolebindings
kubectl describe rolebinding read-pods
```

---

## 🔪 Step 5: Verify Access as Another User

Check if user `jane` has access:

```bash
kubectl auth can-i get pods --as jane
```

Check if user `prashant` has access:

```bash
kubectl auth can-i get pods --as prashant
```

---

## 📁 Step 6: Create and Approve Client Certificate for User

Generate a private key and CSR for the user:

```bash
openssl genrsa -out prashant.key 2048
openssl req -new -key prashant.key -out prashant.csr -subj "/CN=prashant/O=devs"
```

Approve the CSR in Kubernetes:

```yaml
# csr.yaml
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: prashant-csr
spec:
  request: <base64 encoded prashant.csr content>
  signerName: kubernetes.io/kube-apiserver-client
  expirationSeconds: 86400
  usages:
  - client auth
```

Approve it:

```bash
kubectl certificate approve prashant-csr
```

Extract and save the issued certificate:

```bash
kubectl get csr prashant-csr -o jsonpath='{.status.certificate}' | base64 --decode > prashant.crt
```

---

## ⚙️ Step 7: Configure Kubeconfig Context for the User

```bash
kubectl config set-credentials prashant --client-certificate=prashant.crt --client-key=prashant.key
kubectl config set-context prashant --cluster=minikube --namespace=default --user=prashant
kubectl config use-context prashant
```

---

## 🔍 Step 8: Final Verification

Check access as the configured user:

```bash
kubectl auth can-i get pods
```

Expected output: `yes` (since the `pod-reader` role has been bound to this user)

---

## 🧼 Extras

Check role count across all namespaces:

### In PowerShell:

```powershell
kubectl get roles -A --no-headers | Measure-Object -Line
```

### In CMD:

```cmd
kubectl get roles -A --no-headers | wc -l
```

---

✅ **Success**: Successfully created a user, configured cert-based auth, created RBAC roles and bindings, and verified access controls.

