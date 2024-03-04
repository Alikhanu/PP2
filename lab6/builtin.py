# Exercise 1 ----------------------------------------------------
numbers = [1, 2, 3, 4, 5]
result = 1
for num in numbers:
    result *= num
print("The result of multiplying all numbers in the list:", result)
# Exercise 2 ----------------------------------------------------
input_string = input("Enter a string: ")
upper_count = 0
lower_count = 0
for char in input_string:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)
# Exercise 3 ----------------------------------------------------
input_string = input("Enter a string: ")
reversed_string = input_string[::-1]
if input_string == reversed_string:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
# Exercise 4 ----------------------------------------------------
import time
import math
num = 25100
milliseconds = 2123
time.sleep(milliseconds / 1000)
square_root = math.sqrt(num)
print(f"Square root of {num} after {milliseconds} milliseconds is {square_root}")
# Exercise 5 ----------------------------------------------------
my_tuple = (True, True, True)
if all(my_tuple):
    print("All elements of the tuple are true.")
else:
    print("Not all elements of the tuple are true.")
