#Example1----------------------------------------------------
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
#Example2----------------------------------------------------
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
#Example3----------------------------------------------------
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)