#Example1----------------------------------------------------
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
#Example2----------------------------------------------------
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
#Example3----------------------------------------------------
newlist = [x for x in fruits if x != "apple"]
#Example4----------------------------------------------------
newlist = [x for x in fruits]
#Example5----------------------------------------------------
newlist = [x for x in range(10)]
#Example6----------------------------------------------------
newlist = [x for x in range(10) if x < 5]
#Example7----------------------------------------------------
newlist = [x.upper() for x in fruits]
#Example8----------------------------------------------------
newlist = ['hello' for x in fruits]
#Example9----------------------------------------------------
newlist = [x if x != "banana" else "orange" for x in fruits]