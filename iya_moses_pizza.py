import math

def iya_moses_pizza():
    pizza_options = {
        1: {"type": "Sapa size", "price": 2500, "slices": 4},
        2: {"type": "Small Money", "price": 2900, "slices": 6},
        3: {"type": "Big Boys", "price": 4000, "slices": 8},
        4: {"type": "Odogwu", "price": 5200, "slices": 12}
    }

    print("::::::::::::::::::::::::::::::::::::::::::::::::::")
    print("          WELCOME TO IYA MOSES PIZZA JOINT")
    print("::::::::::::::::::::::::::::::::::::::::::::::::::")

    no_of_guests = int(input("How many number of people are attending your party? "))

    print("""
What type of pizza would you like to buy:
    1. Sapa size
    2. Small Money
    3. Big Boys
    4. Odogwu
""")
    pizza_choice = int(input("Kindly enter your choice (1-4): "))

    if pizza_choice not in pizza_options:
        print("We could not find a match for your search, try using another keyword...")
        return

      selected_pizza = pizza_options[pizza_choice]
    pizza_type = selected_pizza["type"]
    price_per_box = selected_pizza["price"]
    slices_per_box = selected_pizza["slices"]

        total_boxes = math.ceil(no_of_guests / slices_per_box)
    total_slices = total_boxes * slices_per_box
    leftover = total_slices - no_of_guests
    total_price = total_boxes * price_per_box
    
    print("____________________::::::::::::::_____________________")
    print("Order summary:")
    print(f"Pizza Type: {pizza_type}")
    print(f"Number of Guests: {no_of_guests}")
    print(f"Boxes Needed: {total_boxes}")
    print(f"Total Slices: {total_slices}")
    print(f"Leftovers: {leftover}")
    print(f"Total Price: {total_price} NGN")
    print("____________________::::::::::::::_____________________")

iya_moses_pizza()
