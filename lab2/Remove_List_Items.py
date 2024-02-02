#Example1----------------------------------------------------
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#Example2----------------------------------------------------
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
#Example3----------------------------------------------------
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#Example4----------------------------------------------------
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#Example5----------------------------------------------------
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#Example6----------------------------------------------------
thislist = ["apple", "banana", "cherry"]
del thislist
#Example7----------------------------------------------------
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)