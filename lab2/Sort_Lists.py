#Example1----------------------------------------------------
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#Example2----------------------------------------------------
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
#Example3----------------------------------------------------
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
#Example4----------------------------------------------------
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
#Example5----------------------------------------------------
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
#Example6----------------------------------------------------
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
#Example7----------------------------------------------------
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
#Example8----------------------------------------------------
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)