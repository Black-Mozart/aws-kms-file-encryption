# aws-kms-file-encryption
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


