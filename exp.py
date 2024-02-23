from math import sqrt

def is_square(num):
    if sqrt(num) == int(sqrt(num)):
        return True

nums = list(range(1, 50))

squares = [x for x in nums if is_square(x) is True ]
print(squares)