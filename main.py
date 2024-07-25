from controllers.auth import signIn, signUp
from colorama import init, Fore, Style
from controllers.todo import getTodos, setTodo, removeTodo, editTodo

# Initialize colorama
init(autoreset=True)

def print_menu():
    """Prints the main menu."""
    print(f"""
    {Fore.CYAN}Welcome to Yash's Todo Console Application
    -------------------------------------------
    {Fore.YELLOW}1. Sign up
    2. Sign in
    3. Exit
    {Style.RESET_ALL}
    """)

def sign_in_menu(username):
    """Displays the todo options menu and processes user choices."""
    while True:
        print(f"""
        {Fore.CYAN}--- Todo Options ---{Style.RESET_ALL}
        {Fore.YELLOW}1. View Todos
        2. Add Todo
        3. Edit Todo
        4. Remove Todo
        5. Sign Out
        {Style.RESET_ALL}
        """)

        try:
            choice = int(input(f"{Fore.MAGENTA}Enter your choice (1-5): {Style.RESET_ALL}"))
        except ValueError:
            print(f"{Fore.RED}ERR: Please enter a valid number.{Style.RESET_ALL}")
            continue

        if choice == 1:
            # View todos
            res = getTodos(username=username)
            print(res)

        elif choice == 2:
            # Add new todo
            title = input(f"{Fore.CYAN}Enter title: {Style.RESET_ALL}").strip()
            desc = input(f"{Fore.CYAN}Enter description: {Style.RESET_ALL}").strip()
            res = setTodo(username=username, title=title, desc=desc)
            print(res)

        elif choice == 3:
            # Edit existing todo
            try:
                todo_id = int(input(f"{Fore.CYAN}Enter todo ID: {Style.RESET_ALL}"))
            except ValueError:
                print(f"{Fore.RED}ERR: Please enter a valid ID.{Style.RESET_ALL}")
                continue
            
            title = input(f"{Fore.CYAN}Enter new title: {Style.RESET_ALL}").strip()
            desc = input(f"{Fore.CYAN}Enter new description: {Style.RESET_ALL}").strip()
            is_completed = input(f"{Fore.CYAN}Is the todo completed (True/False): {Style.RESET_ALL}").strip().lower() in ['true', '1', 'yes']
            res = editTodo(username=username, todo_id=todo_id, title=title, desc=desc, isCompleted=is_completed)
            print(res)
            
        elif choice == 4:
            # Remove todo
            try:
                todo_id = int(input(f"{Fore.CYAN}Enter todo ID: {Style.RESET_ALL}"))
            except ValueError:
                print(f"{Fore.RED}ERR: Please enter a valid ID.{Style.RESET_ALL}")
                continue
            
            res = removeTodo(username=username, todo_id=todo_id)
            print(res)

        elif choice == 5:
            print(f"{Fore.YELLOW}Signing out...{Style.RESET_ALL}")
            break

        else:
            print(f"{Fore.RED}ERR: Invalid choice. Please enter a number between 1 and 5.{Style.RESET_ALL}")

def main():
    """Main function to run the application."""
    while True:
        print_menu()
        try:
            user_choice = int(input(f"{Fore.MAGENTA}Enter your choice (1, 2, 3): {Style.RESET_ALL}"))
        except ValueError:
            print(f"{Fore.RED}ERR: Please enter a valid number.{Style.RESET_ALL}")
            continue

        if user_choice == 1:
            print(f"\n{Fore.GREEN}--- Sign Up ---{Style.RESET_ALL}")
            username = input(f"{Fore.CYAN}Enter username: {Style.RESET_ALL}").strip()
            email = input(f"{Fore.CYAN}Enter email: {Style.RESET_ALL}").strip()
            password = input(f"{Fore.CYAN}Enter password: {Style.RESET_ALL}").strip()

            result = signUp(username, email, password)
            print(f"{Fore.GREEN}{result}{Style.RESET_ALL}")

        elif user_choice == 2:
            print(f"\n{Fore.GREEN}--- Sign In ---{Style.RESET_ALL}")
            username = input(f"{Fore.CYAN}Enter username: {Style.RESET_ALL}").strip()
            password = input(f"{Fore.CYAN}Enter password: {Style.RESET_ALL}").strip()

            result = signIn(username, password)
            print(f"{Fore.GREEN}{result}{Style.RESET_ALL}")

            if result:
                sign_in_menu(username)

        elif user_choice == 3:
            print(f"{Fore.YELLOW}Exiting... Goodbye!{Style.RESET_ALL}")
            break

        else:
            print(f"{Fore.RED}ERR: Invalid choice. Please enter 1, 2, or 3.{Style.RESET_ALL}\n")

if __name__ == "__main__":
    main()
