#Example1----------------------------------------------------
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#Example2----------------------------------------------------
for x in "banana":
  print(x)
#Example3----------------------------------------------------
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#Example4----------------------------------------------------
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
#Example5----------------------------------------------------
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#Example6----------------------------------------------------
for x in range(6):
  print(x)
#Example7----------------------------------------------------
for x in range(2, 6):
  print(x)
#Example8----------------------------------------------------
for x in range(2, 30, 3):
  print(x)
#Example9----------------------------------------------------
for x in range(6):
  print(x)
else:
  print("Finally finished!")
#Example10---------------------------------------------------
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
#Example11---------------------------------------------------
  adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
#Example12---------------------------------------------------
for x in [0, 1, 2]:
  pass
#Exercise1----------------------------------------------------
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#Exercise2----------------------------------------------------
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#Exercise3----------------------------------------------------
for x in range(6):
  print(x)
#Exercise4----------------------------------------------------
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)