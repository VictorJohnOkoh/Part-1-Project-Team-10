"""
This file will be used to hash the passwords entered by the user and be returned for comparison
"""

import bcrypt
"""
this function is used to check if the password entered and the stored password are equal
it's done by using the bcrypt hashing function
"""
def verify_password(password: str, stored_hash: str):
    return bcrypt.checkpw(
        password.encode("utf-8"),
        stored_hash.strip().encode("utf-8")
    )

#this is a function to convert all of the all password to hashes
def hash_password(password: str):
    print(bcrypt.hashpw(password.encode("utf-8"),bcrypt.gensalt()).decode("utf-8"))

#hash_password("hash123")