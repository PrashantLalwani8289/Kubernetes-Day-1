# 🚀 Day 7 - Kubernetes ConfigMap with Environment Variables + Network Security Basics

## 📌 What I'm Learning

Today, I worked on two major areas:
1. **Kubernetes ConfigMaps** and how to inject them into a pod as environment variables.
2. **Core concepts of network security**, focusing on encryption and secure communication protocols (HTTPS, SSH, SSL/TLS).

---

## 🧠 What I Learned

### 🐳 Kubernetes: Injecting ConfigMap Data as Environment Variables

- **ConfigMaps** are used to decouple configuration artifacts from image content to keep containerized applications portable.
- You can create a ConfigMap using `kubectl` and then reference its values inside a pod definition using `env.valueFrom.configMapKeyRef`.
- The value can then be accessed as an environment variable inside the container.

#### ✅ Steps I Followed:

1. **Create the ConfigMap:**

```bash
kubectl create cm app-cm --from-literal=firstname=prashant
```

2. **Verify the ConfigMap:**

```bash
kubectl get cm
kubectl describe cm app-cm
```

3. **Pod YAML snippet using ConfigMap:**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
spec:
  containers:
    - name: myapp-container
      image: busybox:1.28
      command: ['sh', '-c', 'sleep 3600']
      env:
        - name: FIRSTNAME
          valueFrom:
            configMapKeyRef:
              name: app-cm
              key: firstname
```

4. **Apply the Pod manifest:**

```bash
kubectl apply -f pod.yaml
```

5. **Check Pod status:**

```bash
kubectl get po
```

6. **Verify environment variable inside the pod:**

```bash
kubectl exec -it myapp-pod -- sh
echo $FIRSTNAME   # Output: prashant
```

---

### 🔐 Security Concepts

#### 🔒 Why Do We Need HTTPS?

- Prevents **Man-in-the-Middle (MITM)** attacks.
- Protects **data integrity and privacy**.
- Provides **authentication** (via SSL certificates) and **data encryption** (via SSL/TLS).

#### 🔑 Asymmetric vs Symmetric Encryption

| Feature                | Symmetric Encryption | Asymmetric Encryption         |
|------------------------|----------------------|-------------------------------|
| Keys Used              | Single shared key    | Public + Private key pair     |
| Speed                  | Faster               | Slower                        |
| Use Case               | Data encryption at rest | Secure key exchange           |
| Examples               | AES, DES             | RSA, ECC                      |

#### 🔐 How SSH Works with Public-Private Key

- SSH uses **asymmetric encryption**.
- The public key is stored on the server (`~/.ssh/authorized_keys`).
- The private key is kept secret on the client machine.
- When a user tries to SSH:
  1. Server sends a challenge encrypted with the public key.
  2. Client responds with the correct answer using the private key.
  3. If it matches, access is granted without a password.

#### 🔐 How SSL/TLS Works (Simplified)

1. **Client Hello:** Client sends supported TLS version and cipher suites.
2. **Server Hello:** Server responds with its certificate and chosen cipher.
3. **Authentication:** Server certificate is verified.
4. **Key Exchange:** A symmetric key is securely exchanged.
5. **Secure Communication:** All subsequent traffic is encrypted using the shared symmetric key.

---

## 📾 Summary

- Understood how to use Kubernetes **ConfigMaps** to inject configuration into pods using environment variables.
- Practiced with live examples (`kubectl create cm`, `kubectl exec`, and pod YAML).
- Deepened my understanding of **encryption techniques**, **SSH mechanics**, and **HTTPS/SSL/TLS workflows**, which are essential for building secure cloud-native systems.


