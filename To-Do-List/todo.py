 print("Welcome to the To-Do List App baby!")

# Initialize an empty list to store tasks
tasks = []

# Function to display the menu
def show_menu():
	print("\nTo-Do List Menu:")
	print("1. Add a new task")
	print("2. View all tasks")
	print("3. Exit")

# Function to add a task
def add_task():
	task = input("Enter a new task: ")
	tasks.append(task)
	print(f"Task '{task}' added to the list")

# Main program loop
while True:
	show_menu()
	choice = input("Choose an option (1/2/3)")
	
	if choice == "1":
		add_task()
	elif choice == "2":
		print("\nYour Task:")
		for task in tasks:
			print(f"- {task}")
	elif choice == "3":
		print("Exiting the To-Do List App. Goodbye")
		break
	else:
		print("Invalid choice. Please try again")
