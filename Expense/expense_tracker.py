import datetime

def get_date(prompt):
    while True:
        date_input = input(prompt)
        try:
            datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
            return date_input
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD")

def get_valid_amount():
    while True:
        amount = input("Enter the amount: ")
        try:
            return float(amount)
        except ValueError:
            print("Invalid amount. Please try again")

def display_welcome():
    print('''
    Welcome to Semicolon Expense Tracker App
    ----------------------------------------
    ----------------------------------------
    ''')

def display_menu():
    print('''
    1. Add all expenses
    2. View all expenses
    3. Calculate total expenses
    4. Exit
    ''')

def add_expense(expenses):
    date = get_date("Please enter the date in the format YYYY-MM-DD: ")
    description = input("Please enter the description: ")
    amount = get_valid_amount()
    
    expenses.append({
        'date': date,
        'description': description,
        'amount': amount
    })
    print("\nExpense added successfully")

def view_expenses(expenses):
    print('\nAll Expenses:')
    print('-----------------------------------------')
    for index, expense in enumerate(expenses, 1):
        print(f"Expense {index}:")
        print(f"  Date:         {expense['date']}")
        print(f"  Description:  {expense['description']}")
        print(f"  Amount:       ${expense['amount']:.2f}")
        print('-----------------------------------------')

def show_total(expenses):
    total = sum(expense['amount'] for expense in expenses)
    print(f'\nTotal Expenses: ${total:.2f}')

def main():
    expenses = []
    display_welcome()
    
    while True:
        display_menu()
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please enter a number between 1-4")
            continue

        match choice:
            case 1:
                add_expense(expenses)
            case 2:
                view_expenses(expenses)
            case 3:
                show_total(expenses)
            case 4:
                print("Exiting the app. Goodbye")
                break
            case _:
                print("Invalid choice. Please enter 1-4")

main()