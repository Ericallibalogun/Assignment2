def menu_heading():
	print("To-Do List Manager")

def display_menu():
	print('''
	1. Add a task
	2. View all  Tasks
	3. Mark a task as complete
	4. Delete a task
	5. Exit
	''')

def add_task(tasks):
	task = input("Kindly enter the task here: ")

	tasks.append({
		'task': task
	})
	print("Task added")
	
def view_tasks(tasks):
	print("\nAll tasks")
	print("-" * 48)
	for index,task in enumerate(tasks, 1):
		print(f"Task {index}:")
		print(f" [ ]      {task['task']}")
		print("-" * 48)

def mark_complete(tasks):
    print("\nCurrent Tasks:")
    for index, task in enumerate(tasks, 1):
        # Fixed indentation and spacing in checkbox
        print(f"{index}: [{'x' if task['completed'] else ' '}] {task['task']}")
    
    try:
        task_number = int(input("\nEnter the number of the task to mark completed: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number-1]['completed'] = True
            print(f"Task {task_number} marked as complete!")
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a valid number")


def main():
	tasks = []
	menu_heading()

	while True:
		display_menu()

		try:
			choice = int(input("Please enter your choice: "))
		except ValueError:
			print("invalid input.Please enter a number between 1-5 ")
			continue

		match choice:
			case 1:
				add_task(tasks)
			case 2:
				view_tasks(tasks)
			case 3:
				mark_complete(tasks)
			case 5: 
				print("Thanks for using our app")
				break
			case _:
				print("invalid choice.Please enter a number between 1-5 ")
		
main()