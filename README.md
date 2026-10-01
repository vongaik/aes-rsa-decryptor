# AES-RSA Decryptor

## Overview  
I developed a Python algorithm to decrypt a secret message from a dataset of 90,001 AES-encrypted messages, 200 AES keys, and 400 RSA key pairs. The goal was to identify a secret plaintext message by decrypting a large dataset of encrypted files with AES and RSA keys, and verifying with MD5 hashes. My program used RSA private keys to decrypt AES keys, compared the MD5 hash of each decrypted AES key with the provided AES key hash to identify the correct AES key, then used that AES key to decrypt the messages and compared the MD5 hash of each decrypted message with the master message hash to identify the secret message in 16 minutes. 

![setting up AES encryption in CBC mode](<img width="717" height="231" alt="image" src="https://github.com/user-attachments/assets/0d672c09-2454-4ff4-b22b-c9b4fc50597b" />
)

I used AES (CBC mode), RSA (PKCS1_OAEP), and cryptographic hashing to work through the dataset and identify the secret message. Along the way, I tackled nested loop logic, AES padding issues, and decryption performance.

My pseudocode:
<img width="562" height="642" alt="my pseudocode" src="https://github.com/user-attachments/assets/6d879251-0013-4132-9e80-949d7010e9c2" />


## Technologies & Tools  
- **Languages:** Python 3.x  
- **Libraries:** PyCryptodome (AES, PKCS1_OAEP, RSA), hashlib (MD5 hashing)  
- **IDE:** PyCharm  
- **OS:** Windows 10/11  

## Project Description  
The dataset contained:  
- 90,001 encrypted messages (`.emsg`)  
- 200 AES symmetric keys (encrypted) (`.eaes`) 
- 200 RSA public/private key pairs (`.pem`) 
- Two MD5 hash files for AES keys and plaintext messages (`.md5`) 

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
- **Loop Structure:** Infinite loop occurred because of complex triple nested loop structure. _Solution:_ Used double-nested loop for RSA-to_AES, then a single loop for decrypting final message and hash comparison.
- **Debugging Decryption Issues:** Decrypted messages were coming out as garbled, unreadable text because I didn't know which AES mode had been used. _Solution:_ I researched and tested ECB, CFB, and OFB before determining CBC was required. I learned that AES has a fixed 16-byte block size, so CBC requires a 16-byte IV. Using the correct mode and IV produced the correct plaintext. 
- Strengthened my skills in cryptography, including symmetric and asymmetric encryption, as well as Python scripting, debugging, and problem-solving. 

- ## Real-World Security Applications

The automated processing, decryption, and validation workflows in my project directly map to capabilities used in modern cyber security operations:

* **Digital Forensics & Incident Response:** Parsing thousands of unknown files systematically to isolate specific indicators or hidden payloads.
* **Malware Analysis & Ransomware Decryption:** Extracting and validating cryptographic keys, managing block-cipher padding constraints (such as PKCS7), and handling layered encryption methods.
* **Data Integrity Verification:** Using cryptographic hash functions (like MD5) at scale to ensure files have not been corrupted or tampered with during extraction.

