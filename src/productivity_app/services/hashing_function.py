"""
This file will be used to hash the passwords entered by the user and be returned for comparison
"""

import bcrypt

def verify_password(password: str, stored_hash: str):
    return bcrypt.checkpw(
        password.encode("utf-8"),
        stored_hash.strip().encode("utf-8")
    )

#this is a function to convert all of the all password to hashes
def hash_password(password: str):
    return (bcrypt.hashpw(password.encode("utf-8"),bcrypt.gensalt()).decode("utf-8"))

#hash_password("hash123")
hash_password("hash2")
hash_password("hash3")
hash_password('manager1')
