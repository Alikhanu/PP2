#Example1----------------------------------------------------
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#Example2----------------------------------------------------
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#Example3----------------------------------------------------
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#Example4----------------------------------------------------
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)