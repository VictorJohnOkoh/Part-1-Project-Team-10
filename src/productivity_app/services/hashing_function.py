"""
This file will be used to hash the passwords entered by the user and be returned for comparison
"""

import bcrypt

def verify_password(password: str, stored_hash: str):
    return bcrypt.checkpw(
        password.encode("utf-8"),
        stored_hash.strip().encode("utf-8")
    )

def hash_password(password: str):
    print(bcrypt.hashpw(password.encode("utf-8"),bcrypt.gensalt()).decode("utf-8"))

#hash_password("hash123")