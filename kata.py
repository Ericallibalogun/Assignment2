import math
even = int(input("Enter a number to check even/odd: "))
if even % 2 == 0:
        print("It is an even number.")
else:
        print("It is an odd number.")

prime = int(input("Enter a number to check prime: "))
is_prime = True
if prime <= 1:
	is_prime = False
else:
        for number in range(2, int(math.sqrt(prime)) + 1):
            if prime % number== 0:
                is_prime = False
                break
print("It is a prime number." if is_prime else "It is not a prime number.")

    
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
difference = abs(first - second)
print(f"The difference is {difference}")

    
first_quotient = float(input("Enter the first number for division: "))
second_quotient = float(input("Enter the second number for division: "))
if second_quotient == 0:
	print("Division by zero is undefined.")
else:
	quotient = first_quotient / second_quotient
print(f"The quotient is {quotient}")

    
factor = int(input("Enter a number to find its factors: "))
print(f"The factors of {factor} are:")
for number in range(1, factor + 1):
        if factor % number == 0:
            print(number)

    
squared_number = int(input("Enter a number to check if it's a perfect square: "))
square_root = math.sqrt(squared_number)
if square_root.is_integer():
        print("true")
else:
        print("false")

   
integer = int(input("Enter a number to check if it's a palindrome: "))
if str(integer) == str(integer)[::-1]:
        print("The number is a palindrome.")
else:
        print("The number is not a palindrome.")

    
factorial = int(input("Enter a number to calculate its factorial: "))
factorial_result = 1
for number in range(1, factorial + 1):
        factorial_result *= number
        print(f"The factorial of {factorial} is {factorial_result}")

    
the_square = int(input("Enter a number to calculate its square: "))
number_square = the_square ** 2
print(f"The square of {the_square} is {number_square}")



