#Example1----------------------------------------------------
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#Example2----------------------------------------------------
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
#Example3----------------------------------------------------
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
#Example4----------------------------------------------------
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
#Example5----------------------------------------------------
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
#Example6----------------------------------------------------
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
#Example7----------------------------------------------------
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")