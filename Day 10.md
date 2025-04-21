# 🚀 Kubernetes Learning Log – Day 10: ClusterRole vs Role

## 📌 Recap: Authentication vs Authorization

Before we deep dive into **ClusterRole** and **ClusterRoleBinding**, here's a quick recap:

- **Authentication (🔐)**: Verifies *who you are* using:
  - Symmetric key encryption
  - Asymmetric key encryption
  - Certificates

- **Authorization (✅)**: Determines *what you can do*, using:
  - ABAC (Attribute-Based Access Control)
  - RBAC (Role-Based Access Control)
  - Node authorization
  - Webhooks

---

## 🎯 Objective of Today
Understand and implement:
- Difference between `Role` and `ClusterRole`
- Difference between `RoleBinding` and `ClusterRoleBinding`
- Create a custom `ClusterRole` and bind it to a user

---

## 🧠 Key Concepts

### 🔹 Role
- Namespace-scoped
- Permissions are confined to a specific namespace

Example permissions:
```yaml
- list pods
- watch pods
- get pods
```

### 🔹 ClusterRole
- Cluster-scoped (can also be bound to a namespace)
- Used when:
  - You want to define permissions across all namespaces
  - You want to access cluster-scoped resources (like nodes)

Example permissions:
```yaml
- list nodes
- watch nodes
- get nodes
```

### 🔹 RoleBinding
- Binds a `Role` to a `User`, `Group`, or `ServiceAccount` in a **specific namespace**

### 🔹 ClusterRoleBinding
- Binds a `ClusterRole` to a `User`, `Group`, or `ServiceAccount` **across the cluster**

---

## ⚒️ Hands-On: Creating a ClusterRole

### ✅ Command:
```bash
kubectl create clusterrole pod-reader \
  --verb=get,list,watch \
  --resource=pods
```

### ✅ Verification:
```bash
kubectl describe clusterrole pod-reader
```

### ✅ Sample Output:
```yaml
Name:         pod-reader
Labels:       <none>
Annotations:  <none>
PolicyRule:
  Resources:  pods
  Verbs:      get, list, watch
```

---

## 👤 Dummy User: `prashant`
Let’s create a `ClusterRoleBinding` for this user.

### ✅ Command:
```bash
kubectl create clusterrolebinding prashant-global-pod-reader \
  --clusterrole=pod-reader \
  --user=prashant
```

### ✅ Verification:
```bash
kubectl describe clusterrolebinding prashant-global-pod-reader
```

### ✅ Sample Output:
```yaml
Name:         prashant-global-pod-reader
Subjects:
  Kind:       User
  Name:       prashant
Role:
  Kind:       ClusterRole
  Name:       pod-reader
```

---

## 🧪 Testing Permissions
To verify that `prashant` has access:

```bash
kubectl auth can-i list pods --as=prashant
```
Output should be:
```
yes
```

---

## 📌 When to Use What?
| Scenario                                  | Use             |
|-------------------------------------------|------------------|
| Read pods in a specific namespace         | Role + RoleBinding |
| Read pods in all namespaces               | ClusterRole + ClusterRoleBinding |
| List all nodes in the cluster             | ClusterRole + ClusterRoleBinding |
| Different permissions per namespace       | Separate Roles & RoleBindings |

---

## 🧩 Extra: YAML Manifest Example

### ClusterRole YAML:
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: secret-reader
rules:
- apiGroups: [""]
  resources: ["secrets"]
  verbs: ["get", "list"]
```

### ClusterRoleBinding YAML:
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: read-secrets-binding
subjects:
- kind: User
  name: dummy-user
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: secret-reader
  apiGroup: rbac.authorization.k8s.io
```

---

## 📚 Summary
- Roles are **namespace-scoped**, ClusterRoles are **cluster-scoped**
- Use **RoleBinding** for namespace-level permissions
- Use **ClusterRoleBinding** for global (cluster-wide) permissions
- Easy to test with `kubectl auth can-i` command

---

👉 Next I’ll dive into **Service Accounts** and how to combine them with `RoleBindings` and `ClusterRoleBindings` for secure automated workflows.

