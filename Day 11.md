# 🚀 Kubernetes Day 11 — ServiceAccounts, Roles & RBAC in Action

Today’s focus was on working with **ServiceAccounts**, **Secrets**, **RBAC**, and impersonation using `--as`. Below is a complete walkthrough of what I covered, with examples and outputs.

---

## 🔹 1. Listing All Service Accounts

### ✅ Get service accounts in the current namespace
```bash
kubectl get sa
```

### ✅ Get service accounts in **all namespaces**
```bash
kubectl get sa -A
```

### ✅ Filter for `default` service accounts (PowerShell)
```powershell
kubectl get sa -A | Select-String "default"
```

---

## 🔹 2. Describing Service Accounts

```bash
kubectl describe sa default
```

---

## 🔹 3. Creating a Custom Service Account

```bash
kubectl create sa build-sa
```

### Confirm creation:
```bash
kubectl get sa
kubectl describe sa build-sa
```

---

## 🔹 4. Creating a Secret Token for the Service Account

### secret.yaml
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: build-robot-secret
  annotations:
    kubernetes.io/service-account.name: build-sa
type: kubernetes.io/service-account-token
```

### Apply the YAML:
```bash
kubectl apply -f secret.yaml
```

### Verify:
```bash
kubectl get secret
kubectl describe secret/build-robot-secret
```

---

## 🔹 5. Trying Access with `--as` Flag

```bash
kubectl get pods --as build-sa
```

> ❌ **Error: Forbidden** — because permissions were not granted yet

---

## 🔹 6. Creating RBAC Roles and Bindings

### ✅ Create Role
```bash
kubectl create role build-role --verb=list,watch,get --resource=pod
```

### ✅ Create RoleBinding
```bash
kubectl create rolebinding rb --role=build-role --user=build-sa
```

---

## 🔹 7. Test Access Again Using `--as`

### 🔍 Try to get pods
```bash
kubectl get pods --as build-sa
```

> ✅ Should now be able to access the pods (if there are any)

---

## 🔹 8. Authorization Check

```bash
kubectl auth can-i get pods --as build-sa
```

> ✅ Output: `yes` — confirms that RBAC is working as expected

---

## 🧠 Key Takeaways

- `kubectl get sa -A` lists **all service accounts** across namespaces.
- PowerShell doesn't support `grep`; use `Select-String` instead.
- To grant a ServiceAccount permissions, you must use **Roles** and **RoleBindings**.
- You can impersonate a ServiceAccount using `--as <sa-name>`.
- Creating a Secret of type `kubernetes.io/service-account-token` binds a token to a ServiceAccount.




