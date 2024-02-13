#Exercise1----------------------------------------------------
def g_to_o(grams):
    return 28.3495231 * float(grams)

grams = input("How many grams? ")
ounces = g_to_o(grams)
print ("It is",ounces, "ounces" )
#Exercise2----------------------------------------------------
def F_to_C(Fahrenheit):
    return (float(Fahrenheit) - 32) * (5 / 9)
Fahrenheit = input("How many Fahrenheit? ")
Celsius  = F_to_C(Fahrenheit)
print("It is",Celsius ,"celsius ")
#Exercise3----------------------------------------------------
def solve(numheads, numlegs):
    rabbits = (numlegs - 2 * numheads)/2
    chikens = numheads - rabbits
    print ("We have",rabbits,"rabbits and",chikens,"chikens")
solve(35,94)
#Exercise4----------------------------------------------------
def filter_prime(list):
    new = []
    prime = True
    for i in list:
        if i==1:
            new.append(i)
        else:
            for j in range(2,i):
                if (i % j) == 0:
                    prime = False
                    break
            if prime:
                new.append(i)
        prime = True
    print (new)

forth_input = input("Enter numbers: ")
new_forth_input = [int(i) for i in forth_input.split()]
filter_prime(new_forth_input)
#Exercise5----------------------------------------------------
from itertools import permutations

def print_permutations(string):
    for perm in permutations(string):
        print(''.join(perm))

fifth_input = input("Enter word: ")
print_permutations(fifth_input)
#Exercise6----------------------------------------------------
def reverse(sentence):
    words = sentence.split()
    new = ' '.join(reversed(words))
    return new

sixth_input = input("Enter sentences: ")
reversed_sentences = reverse(sixth_input)
print(reversed_sentences)
#Exercise7----------------------------------------------------
def has_adjacent_3(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

seventh_input = input("Enter numberrs: ")
new_seventh_input = [int(num) for num in seventh_input.split()]
print(has_adjacent_3(new_seventh_input))
#Exercise8----------------------------------------------------
def contains_007(numbers):
    z=0
    
    for num in numbers:
        if num == 0:
            z += 1
        elif num == 7 and z>=2:
            return True
    
    return False

eighth_input = input("Enter numbers: ")
new_eighth_input = [int(num) for num in eighth_input.split()]
print(contains_007(new_eighth_input))
#Exercise9----------------------------------------------------
import math

def formula(radius):
    return (4/3) * math.pi * radius**3

radius = float(input("Enter radius: "))
volume = formula(radius)
print("The volume is:", volume)
#Exercise10---------------------------------------------------
def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

tenth_input = input("Enter list: ")
new_tenth_input = [int(item) for item in tenth_input.split()]
result = unique_elements(new_tenth_input)
print(result)
#Exercise11---------------------------------------------------
def is_palindrome(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]

eleventh_input = input("Enter word: ")
if is_palindrome(eleventh_input):
    print(eleventh_input ,"is a palindrome.")
else:
    print(eleventh_input ,"is not a palindrome.")
#Exercise12---------------------------------------------------
def histogram(numbers):
    for num in numbers:
        print('*' * num)

# Example usage with user input:
twelfth_input = input("Enter integers: ")
new_twelfth_input = [int(num) for num in twelfth_input.split()]
histogram(new_twelfth_input)
#Exercise13---------------------------------------------------
import random

def guess_the_number():
    secret_number = random.randint(1, 20)
    
    name = input("Hello! What is your name? ")
    print("Well,",name,", I am thinking of a number between 1 and 20.\nTake a guess.")
    
    attempts = 0
    while True:
        guess = int(input())
        attempts += 1
        
        if guess < secret_number:
            print("Your guess is too low.\nTake a guess.")
        elif guess > secret_number  :
            print("Your guess is too high.\nTake a guess.")
        else:
            print("Good job,",name,"! You guessed my number in",attempts," guesses!")
            break

guess_the_number()
#Exercise14---------------------------------------------------
