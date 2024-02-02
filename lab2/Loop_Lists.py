#Example1----------------------------------------------------
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#Example2----------------------------------------------------
  thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
#Example3----------------------------------------------------
  thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
#Example4----------------------------------------------------
  thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]