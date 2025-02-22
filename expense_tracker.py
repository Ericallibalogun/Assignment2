import datetime

def get_date(prompt):
    while True:
        date_input = input(prompt)
        try:
            datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
            return date_input
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD")



def main():
    user_details = []
    print('''
    Welcome to Semicolon Expense Tracker App
    ----------------------------------------
    ''')
    while True:
        print('''
    1. Add all expenses
    2. View all expenses
    3. Calculate total expenses
    4. Exit
    ''')

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please enter a number between 1 - 4")
            continue


        match choice:
            case 1:

                date = input("Please enter the date in the format YYYY-MM-DD: ")
                description = input("Please the description: ")

                while True:
                    amount = input("Enter the amount:")
                    try:
                        amount = float(amount)
                        break
                    except ValueError:
                        print("Invalid amount. Please try again")

                user_details.append({
                    'date': date,
                    'description': description,
                    'amount': amount
                })
                print("\nExpense added successfully")

            case 2:
                print('''
                All Expenses:
                -----------------------------------------
                ''')
                for index,expense in enumerate(user_details, 1):
                    print(f"Expense {index}:")
                    print(f"  Date:         {expense["date"]}")
                    print(f"  Description:  {expense['description']}")
                    print(f"  Amount:       ${expense['amount']:.2f}")
                    print(' -----------------------------------------')

            case 3:
                total = sum(expense['amount'] for expense in user_details)
                print(f'\nTotal Expenses: {total: .2f}')

            case 4:
                print("Exiting the app.Goodbye")
                break
            case _:
                print("Invalid choice.Please enter 1 - 4")






if __name__ == '__main__':
        main()
