#Example1----------------------------------------------------
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
#Example2----------------------------------------------------
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
#Example3----------------------------------------------------
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
#Example4----------------------------------------------------
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
#Example5----------------------------------------------------
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)