
from peewee import IntegrityError, DoesNotExist
from models.user import User
from utils.password import hashPassword, verifyPassword


def signUp(username: str, email: str, password: str) -> str:
    try:
        # Hash the password before saving 
        hashed_password = hashPassword(password)
        
        # Create a new user
        user = User.create(username=username, email=email, password=hashed_password)
        
        # If user is created successfully, return True
        return f"Username {user.username} has been created successfully"
        
    except IntegrityError:
        # Handle unique constraint violation (e.g., username already exists)
        return "ERR: Username already exists."
        
    except Exception as e:
        # Handle other exceptions
        return f"ERR: {e}"


def signIn(username:str, password:str) -> str:
    try:
        user = User.get(User.username == username)
        
        if verifyPassword(user.password, password):
            return f"User {user.username} signed in successfully."
        else:
            return "ERR: Incorrect password."
    
    except DoesNotExist:
        return "ERR: Username does not exist."
        
    except Exception as e:
        return f"ERR: {e}"
