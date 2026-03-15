import boto3
import os

# ---------- Config ----------
kms_key_arn = "YOUR_KMS_KEY_ARN"
input_file = "secret1.txt"
encrypted_file = "output/secret1.txt.encrypted"
decrypted_file = "output/secret1.txt.encrypted.decrypted"

# Ensure output directory exists
os.makedirs("output", exist_ok=True)

# Read plaintext file
with open(input_file, "rb") as f:
    plaintext = f.read()

# Connect to AWS KMS
kms_client = boto3.client("kms", region_name="us-west-2")

# Encrypt the file
encrypt_response = kms_client.encrypt(
    KeyId=kms_key_arn,
    Plaintext=plaintext,
    EncryptionContext={"purpose": "test"}
)

ciphertext = encrypt_response["CiphertextBlob"]

with open(encrypted_file, "wb") as f:
    f.write(ciphertext)

print(f"Encrypted file written to {encrypted_file}")

# Decrypt the file
decrypt_response = kms_client.decrypt(
    CiphertextBlob=ciphertext,
    EncryptionContext={"purpose": "test"}
)

decrypted_text = decrypt_response["Plaintext"]

with open(decrypted_file, "wb") as f:
    f.write(decrypted_text)

print(f"Decrypted file written to {decrypted_file}")

# Verify result
with open(decrypted_file, "r") as f:
    print("Decrypted content:", f.read())
