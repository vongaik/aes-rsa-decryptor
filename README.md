# Ethical Hacking Milestone 4: Secret Message Decryption

## Overview  
This project demonstrates practical application of cryptography concepts—specifically symmetric and asymmetric encryption—using Python. The goal was to identify a secret plaintext message by decrypting a large dataset of encrypted files with AES and RSA keys, and verifying with MD5 hashes.

I leveraged knowledge of AES (CBC mode), RSA (PKCS1_OAEP), and cryptographic hashing to crack the code in a systematic, layered approach. This project highlights skills in Python programming, cryptographic libraries, problem-solving, debugging encryption issues, and data verification.

## Technologies & Tools  
- **Languages:** Python 3.x  
- **Libraries:** PyCryptodome (AES, PKCS1_OAEP, RSA), hashlib (MD5 hashing)  
- **IDE:** PyCharm  
- **OS:** Windows 10  

## Project Description  
The dataset contained:  
- 90,001 encrypted messages (`.emsg`)  
- 200 AES symmetric keys (encrypted)  
- 400 RSA public/private key pairs  
- Two MD5 hash files for AES keys and plaintext messages  

The task was to:  
1. Decrypt AES keys using RSA private keys.  
2. Verify decrypted AES keys by comparing MD5 hashes.  
3. Use verified AES keys to decrypt the messages.  
4. Compute MD5 hashes of decrypted messages to find the secret message matching the master hash.  

## Methodology  
- **Layered Decryption:**  
  - First, RSA was used to decrypt AES keys via PKCS1_OAEP.  
  - Then, AES keys decrypted messages in CBC mode with a professor-provided IV.  
- **Verification:** MD5 hashes ensured the integrity and correctness of keys and messages.  
- **Debugging:** Overcame initial padding issues during AES decryption by troubleshooting block size and padding compatibility.  
- **AI Assistance:** Consulted AI tools to clarify cryptography concepts and solve specific implementation challenges.

## Execution Flow  
1. Load RSA private key from PEM files.  
2. Decrypt AES keys with RSA.  
3. Check AES key hash against provided hash file.  
4. Decrypt encrypted messages using verified AES key.  
5. Compute MD5 hash of each decrypted message.  
6. Identify the secret message by matching its hash with the master hash.  

## Challenges & Learnings  
- Debugged padding errors common in AES CBC mode decryptions.  
- Improved understanding of RSA and AES cryptographic workflows.  
- Applied cryptographic hash functions for secure verification.  
- Enhanced Python skills in handling file I/O and cryptographic operations on large datasets.
