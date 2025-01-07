def checkout():
    print("Enter the cashier's name: ", end="")
    cashier_name = input()

    print("What is the customer's name? ", end="")
    customer_name = input()

    print("_______________________________________________")
    print("SEMICOLON STORES")
    print("MAIN BRANCH")
    print("LOCATION: HERBERT MACAULAY WAY, SABO YABA, LAGOS.")
    print("TEL: 03293828343")
    print("Date : 18-Dec-22  8:48:11 pm")
    print("Cashier: ", cashier_name)
    print("Customer's Name: ", customer_name)
    print("_______________________________________________")
    print(f"{'ITEM':<15} {'QTY':<5} {'PRICE':<10} {'TOTAL (NGN)':<10}")

    total_cost = 0

    while True:
        print("\nWhat did the user buy? ", end="")
        customer_purchase = input()

        print("How many pieces? ", end="")
        quantity = int(input())

        print("How much per unit? ", end="")
        price = float(input())

        item_cost = quantity * price
        total_cost += item_cost

        print("_______________________________________________")
        print(f"{customer_purchase:<15} {quantity:<5} {price:<10.2f} {item_cost:<10.2f}")
        print("_______________________________________________")

        print("Do you want to add more items? (yes/no): ", end="")
        response = input()
        if response.lower() != "yes":
            break

    discount = total_cost * 0.08
    vat = total_cost * 0.175
    total = total_cost + vat - discount

    print("_______________________________________________")
    print(f"{'Total Cost:':<25} {total_cost:<10.2f}")
    print(f"{'Discount:':<25} {discount:<10.2f}")
    print(f"{'VAT @ 17.50%:':<25} {vat:<10.2f}")
    print(f"{'Total:':<25} {total:<10.2f}")
    print("_______________________________________________")

    print("Input the amount paid: ", end="")
    amount_paid = float(input())
    balance = amount_paid - total
    print("_______________________________________________")
    print(f"{'Amount Paid:':<25} {amount_paid:<10.2f}")
    print(f"{'Balance:':<25} {balance:<10.2f}")
    print("_______________________________________________")
    print("THANK YOU FOR YOUR PATRONAGE")

checkout()
