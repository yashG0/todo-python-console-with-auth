from peewee import IntegrityError, DoesNotExist
from models.tweet import Todo
from models.user import User
from tabulate import tabulate


def setTodo(username: str, title: str, desc: str) -> str:
    try:
        # Retrieve user by username
        user = User.get(User.username == username)

        # Create a new Todo item
        todo = Todo.create(user=user, title=title, desc=desc)
        return f"Todo '{todo.title}' created successfully."

    except DoesNotExist:
        return "ERR: User not found."

    except Exception as e:
        return f"ERR: {e}"

def getTodos(username: str) -> str:
    try:
        # Retrieve user by username
        user = User.get(User.username == username)

        # Retrieve todos for the specific user
        todos = Todo.select().where(Todo.user == user)

        if todos.exists():
            # Prepare data for tabulate
            table_data = []
            for todo in todos:
                status = "Completed" if todo.isCompleted else "Pending"
                table_data.append([todo.id, todo.title, todo.desc[0:75], status])

            # Create table with headers
            headers = ["ID", "Title", "Description", "Status"]
            return tabulate(table_data, headers=headers, tablefmt="fancy_grid")

        else:
            return "No todos found."

    except DoesNotExist:
        return "ERR: User not found."

    except Exception as e:
        return f"ERR: {e}"

def editTodo(username: str, todo_id: int, title: str, desc: str, isCompleted: bool|None = None) -> str:
    try:
        # Retrieve user by username
        user = User.get(User.username == username)
        
        # Retrieve the todo item
        todo = Todo.get(Todo.id == todo_id, Todo.user == user)
        
        # Update fields if provided
        if title is not None:
            todo.title = title
        if desc is not None:
            todo.desc = desc
        if isCompleted is not None:
            todo.isCompleted = isCompleted
        todo.save()
        return f"Todo with ID {todo_id} updated successfully."
        
    except DoesNotExist:
        return "ERR: User or Todo not found."
        
    except Exception as e:
        return f"ERR: {e}"

def removeTodo(username: str, todo_id: int) -> str:
    try:
        # Retrieve user by username
        user = User.get(User.username == username)
        
        # Retrieve and delete the todo item
        todo = Todo.get(Todo.id == todo_id, Todo.user == user)
        
        todo.delete_instance()
        return f"Todo with ID {todo_id} removed successfully."
        
    except DoesNotExist:
        return "ERR: User or Todo not found."

    except Exception as e:
        return f"ERR: {e}"
