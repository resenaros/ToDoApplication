"""
To-Do List Application
----------------------
A simple command-line application to manage a to-do list.
Users can add, view, or delete tasks. 
Tasks are stored in a list and the app handles invalid input gracefully.
"""

# Pre-populated list for testing and demonstration purposes
tasks = ["Do Homework", "Code Video Game", "Walk Dog"]

def display_menu():
    """Displays the main menu options to the user"""
    print("\nTo-Do List Application Main Menu:\n")
    print("1: Add Task")
    print("2: View Task")
    print("3: Delete Task")
    print("4: Exit Application")
    
def add_task():
    """Prompts the user for a task, formats it, and adds it to the task list if valid."""
    task=input("\nWhat task would you like to add to your list? ").strip()
    # Validate user input to ensure it's not just whitespace
    if task.strip() == "":
        print("\nTask cannot be empty.")
        return
    # Capitalize first letter of each word for uniformity
    formatted_task = task.title()
    # Convert task to title case to maintain consistency (e.g., "walk dog" ➡️ "Walk Dog")
    tasks.append(formatted_task)  # Adds the task to the end of the list
    print(f"\n'{formatted_task}' has been added to the list")
    print("\nUpdated task list:")
    view_task()


def view_task():
    """Displays all current tasks in the task list, or a message if the list is empty."""
    if not tasks:
        # Notifies user if there are no more tasks
        print("\nThere are currently no tasks in the task list.")
    else:
        print("\nHere are your current tasks in your list: \n")
        # Enumerate through tasks and display each starting at 1 to align how users count (not zero-indexed)
        for i, task in enumerate(tasks, 1):
            print(f"{i}: {task}")
            
def delete_task():
    """Displays current tasks and lets the user delete one by entering its number, with confirmation."""
    view_task() # Shows current tasks before asking which to delete
    if tasks:
        try:
            idx=int(input("\nEnter task number to delete: ")) -1 # Converts to a zero-based index
            # Try converting user input to integer and adjust for zero-based indexing
            if 0 <= idx < len(tasks):
                task_to_delete = tasks[idx]
                # Confirmation loop: asks the user to confirm their choice 
                # (e.g., deleting a task) until valid input ('y' or 'n') is received.
                while True:
                    confirm = input (f"\nAre you sure you want to delete '{task_to_delete}'? (y/n): ").strip().lower()
                    if confirm == 'y':
                        removed_task = tasks.pop(idx) # Removes the selected task
                        print(f"\nTask '{removed_task}' was deleted successfully.")
                        print("\nUpdated task list:")
                        view_task()
                        break
                    elif confirm == 'n':
                        print("\nTask deletion canceled.")
                        break
                    else:
                        print("\nInvalid input. Please enter 'y' or 'n'.")    
            else:
                print("\nInvalid Task Number") # Index is out of range
        except ValueError:
            # Handles non-numeric inputs
            print("\nInvalid input. Please enter a valid number")

def main():
    """Main function to run the To-Do List application"""
    print("Welcome to the To-Do List Application!") # Greeting message
    print("--------------------------------------")
    # Application loop begins and will continue until the user confirms exit
    while True:
        
        display_menu() # Shows menu options
        show_return_msg = True # Flag to control finally print message
        try:
            # Prompts the user for a choice
            choice = int(input("\nWhat would you like to do? "))
        except ValueError:
            # Handles cases where input is not an integer
            print("\nThat is not a valid number.") 
        else:
            # Executes the corresponding function based on user input
            if choice == 1:
                add_task()
            elif choice == 2:
                view_task()  
            elif choice == 3:
                delete_task()  
            elif choice == 4:
                # Confirmation loop: asks the user to confirm their choice 
                # (e.g., exiting) until valid input ('y' or 'n') is received.
                while True:
                    confirm = input("\nAre you sure you want to exit? (y/n): ").strip().lower()
                    if confirm == 'y':
                        print("\nYou are exiting the application. Goodbye!")
                        show_return_msg = False
                        return # Exits the entire main() function and ends the program
                    elif confirm == 'n':
                        print("\nExit canceled.")
                        break
                    else:
                        print("\nInvalid input. Please enter 'y' or 'n'.")
            else:
                print("\nThat's not a valid input") # Handles menu options out of the pre-determined range
        finally:
            # Always return to menu unless exiting
            if show_return_msg:
                print("\nReturning to the main menu...")

# Entry point: Runs the application

main()