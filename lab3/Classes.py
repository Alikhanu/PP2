#Exercise1----------------------------------------------------
class String:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print("String in upper case:", self.string.upper())

controller = String()
controller.getString()
controller.printString()
#Exercise2----------------------------------------------------
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length * self.length

shape = Shape()
print("Area of shape:", shape.area())

a = int(input("Enter lengt: "))
square = Square(a)
print("Area of square:", square.area())
#Exercise3----------------------------------------------------
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

a = int(input("Enter lengt: "))
b = int(input("Enter width: "))
rectangle = Rectangle(a, b)
print("Area of rectangle:", rectangle.area())
#Exercise4----------------------------------------------------
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("Coordinates of the point:",self.x,",",self.y,)

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        return distance


x1 = float(input("Enter x-coordinate for point 1: "))
y1 = float(input("Enter y-coordinate for point 1: "))
point1 = Point(x1, y1)

x2 = float(input("Enter x-coordinate for point 2: "))
y2 = float(input("Enter y-coordinate for point 2: "))
point2 = Point(x2, y2)

point1.show()
point2.show()

print("Distance between the points:", point1.dist(point2))

x3 = float(input("Enter x-coordinate for point 3: "))
y3 = float(input("Enter y-coordinate for point 3: "))
point1 = Point(x3, y3)
point1.move(x3, y3)
point1.show()
#Exercise5----------------------------------------------------
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ${amount} accepted. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please deposit a positive amount.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal of ${amount} accepted. New balance: ${self.balance}")
            else:
                print("Insufficient funds. Withdrawal denied.")
        else:
            print("Invalid withdrawal amount. Please withdraw a positive amount.")

account = BankAccount("John")
account.deposit(100)
account.withdraw(50)
account.withdraw(70)
account.deposit(-40)
account.deposit(200)
account.withdraw(300)
#Exercise6----------------------------------------------------
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

user_input = input("Enter numbers list: ")
numbers = [int(i) for i in user_input.split()]

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Prime numbers in the list:", prime_numbers)