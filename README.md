
Encrypt and decrypt files using AWS Key Management Service (KMS) with Python and boto3. 

# AWS KMS File Encryption Project
## Overview

This project demonstrates how to encrypt and decrypt files using AWS Key Management Service (KMS) with Python.

The goal is to simulate protecting sensitive data stored in files using cloud-managed encryption keys.

The project uses the AWS SDK for Python (boto3) to send data to AWS KMS for encryption and decryption.


## Problem

Sensitive data stored in files can be exposed if unauthorized users gain access to the system.

Organizations must protect confidential information such as:

1) passwords
2) API keys
3) financial data
4) customer record

Without encryption, this information can be easily read.

## Solution

AWS Key Management Service (KMS) provides managed encryption keys that allow applications to encrypt and decrypt data securely.

This project demonstrates how to:

1) Read a file containing sensitive information

2) Encrypt the data using an AWS KMS key

3) Store the encrypted data

4) Decrypt the data to recover the original content

This ensures that sensitive information is stored securely as ciphertext.


### Technologies Used

1) Python

2) AWS Key Management Service (KMS)

3) boto3 (AWS SDK for Python)

4) Git

5) Linux command line

# HOW IT WORKS

## workflow
[Plaintext File: secret1.txt] ---> [Encrypt using AWS KMS] ---> [Encrypted File: secret1.txt.encrypted] ---> [Decrypt using AWS KMS] ---> [Decrypted File: secret1.txt.encrypted.decrypted] 


# Explanation
1) Plaintext File – The file you want to protect (secret1.txt).
2) Encrypt – Your Python script sends the data to AWS KMS for encryption.
3) Encrypted File – The encrypted output is unreadable without access to the KMS key.
4) Decrypt – The script sends the ciphertext to AWS KMS to recover the original data.
5) Decrypted File – Restores the plaintext to secret1.txt.encrypted.decrypted for verification.


