import base64

# Your secret key
secret_key = "cm0t7oK8Jm2KF9GTn1VEPp4a_l-hrW_WwdG_BdIfCQ8"

# Encoding to base64
encoded_key = base64.b64encode(secret_key.encode()).decode()

print(encoded_key)