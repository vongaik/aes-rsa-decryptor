# Vongai Kwenda
# 18 Nov 2024
# Milestone 4

# import libraries - won't use padding library
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
import hashlib
import os

# Load RSA private key
def load_rsa_private_key(file_path):
    with open(file_path, 'r') as priv_key_file:
        private_key = RSA.import_key(priv_key_file.read())
    return private_key

# Decrypt AES key using RSA
def decrypt_aes_key_with_rsa(encrypted_aes_key, private_key):
    cipher_rsa = PKCS1_OAEP.new(private_key)
    return cipher_rsa.decrypt(encrypted_aes_key)

# Load AES-encrypted message
def load_encrypted_message(file_path):
    with open(file_path, 'rb') as enc_file:
        return enc_file.read()

# Decrypt the message using AES in CBC mode with a fixed IV
def decrypt_message_with_aes_cbc(encrypted_message, aes_key):
    iv = 16 * b'\x00'  # Fixed IV as specified
    cipher = AES.new(aes_key, AES.MODE_CBC, iv)
    decrypted_message = b""
    for i in range(0, len(encrypted_message), AES.block_size):
        chunk = encrypted_message[i:i + AES.block_size]
        decrypted_message += cipher.decrypt(chunk)
    return decrypted_message

# Hash the decrypted AES key using MD5
def hash_decrypted_aes_key(aes_key):
    return hashlib.md5(aes_key).hexdigest()

# Verify hash of decrypted message
def verify_hash(decrypted_data, hash_file_path):
    with open(hash_file_path, 'r') as hash_file:
        expected_hash = hash_file.read().strip()
    computed_hash = hashlib.md5(decrypted_data).hexdigest()
    return expected_hash == computed_hash

# Main function
def main():
    # Paths to folders
    rsa_folder = 'rsa'
    aes_folder = 'aes'
    messages_folder = 'messages'
    hashes_folder = 'hashes'

    # Files for validation
    master_message_hash_file = os.path.join(hashes_folder, 'plain_master_message_hash.md5')
    aes_hash_file = os.path.join(hashes_folder, 'plain_aes_hash.md5')

    # Get the first 200 RSA private key files
    rsa_files = [f for f in os.listdir(rsa_folder) if f.endswith('.pem')][:200]

    correct_aes_key = None  # Placeholder for the correct AES key

    # Loop 1: Iterate over RSA private key files
    for private_key_file in rsa_files:
        private_key_path = os.path.join(rsa_folder, private_key_file)
        try:
            private_key = load_rsa_private_key(private_key_path)
            print(f"Trying RSA private key: {private_key_file}")
        except Exception as e:
            print(f"Error loading RSA private key {private_key_file}: {e}")
            continue

        # Loop 2: Iterate over AES key files
        for aes_key_file in os.listdir(aes_folder):
            aes_key_path = os.path.join(aes_folder, aes_key_file)

            try:
                with open(aes_key_path, 'rb') as aes_file:
                    encrypted_aes_key = aes_file.read()
            except FileNotFoundError:
                print(f"AES key file {aes_key_file} not found.")
                continue

            # Decrypt AES key
            try:
                aes_key = decrypt_aes_key_with_rsa(encrypted_aes_key, private_key)
                print(f"AES key decrypted successfully.")  # printing allows me to see where i am in process
            except Exception as e:
                print(f"Error decrypting AES key {aes_key_file} with RSA: {e}")
                continue

            # Validate AES key hash
            if hash_decrypted_aes_key(aes_key) == open(aes_hash_file).read().strip():
                print("Correct AES key found!")
                correct_aes_key = aes_key
                break  # Exit Loop 2 once correct AES key is found

        if correct_aes_key:  # Exit Loop 1 if AES key is found
            break

    if not correct_aes_key:
        print("Correct AES key not found. Exiting.")
        return

    # Loop 3: Decrypt messages using the correct AES key
    for message_file in os.listdir(messages_folder):
        message_path = os.path.join(messages_folder, message_file)

        try:
            encrypted_message = load_encrypted_message(message_path)
        except FileNotFoundError:
            print(f"Encrypted message file {message_file} not found.")
            continue

        # Decrypt message
        try:
            decrypted_message = decrypt_message_with_aes_cbc(encrypted_message, correct_aes_key)
            unpadded_message = decrypted_message  # Assuming padding is removed
            print(f"Decrypted message from {message_file}:", unpadded_message.decode('utf-8', errors='ignore'))

            # Verify message hash
            if verify_hash(unpadded_message, master_message_hash_file):
                print("Secret message found!")
                print("Secret message:", unpadded_message.decode('utf-8'))
                break  # Stop after finding the correct message
            else:
                print(f"Hash mismatch for message in {message_file}. Moving to the next message.")

        except Exception as e:
            print(f"Error decrypting message from {message_file}: {e}")
            continue


if __name__ == "__main__":
    main()

