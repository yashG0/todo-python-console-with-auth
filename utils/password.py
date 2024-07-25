import bcrypt

def hashPassword(password: str) -> str:
    # Hash the password using bcrypt.
    
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')
    
    
def verifyPassword(hashPassword: str, password: str) -> bool:
    # Verify the password against the stored hash.
    return bcrypt.checkpw(password.encode('utf-8'), hashPassword.encode('utf-8'))
