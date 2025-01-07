numbers = [34, 56, 78, 90, 23, 54]

maximum = numbers[0]
for number in numbers:
    if number > maximum:
        maximum = number
print("\nThe largest element is:", maximum)

minimum = numbers[0]
for number in numbers:
    if number < minimum:
        minimum = number
print("\nThe smallest element is:", minimum)

total_sum = sum(numbers)
print("\nThe sum of the elements is:", total_sum)

odd_numbers = [number for number in numbers if number % 2 != 0]
sum_of_odd_numbers = sum(odd_numbers)
print("\nThe odd numbers are:", odd_numbers)
print("Total number of odd numbers:", len(odd_numbers))
print("The sum of odd numbers is:", sum_of_odd_numbers)

even_numbers = [number for number in numbers if number % 2 == 0]
sum_of_even_numbers = sum(even_numbers)
print("\nThe even numbers are:", even_numbers)
print("Total number of even numbers:", len(even_numbers))
print("The sum of even numbers is:", sum_of_even_numbers)

squares = [number ** 2 for number in numbers]
print("\nThe square of the numbers are:", squares)
