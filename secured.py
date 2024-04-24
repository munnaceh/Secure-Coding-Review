import secrets
import hashlib

# Generate a 256-bit random number
key = secrets.randbits(8 * 32)

# Convert the random number to a string
key_str = f'{key:0{32}x}'

# Compute the SHA-256 hash of the string
hash_obj = hashlib.sha256(key_str.encode())
hash_hex = hash_obj.hexdigest()

# Print the SHA-256 hash
print(hash_hex)
