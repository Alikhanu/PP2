#Example1----------------------------------------------------
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#Example2----------------------------------------------------
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#Example3----------------------------------------------------
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
#Example4----------------------------------------------------
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
#Example5----------------------------------------------------
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
#Example6----------------------------------------------------
tuple1 = ("abc", 34, True, 40, "male")
#Example7----------------------------------------------------
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
#Example8----------------------------------------------------
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)