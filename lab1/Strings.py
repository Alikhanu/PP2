#Example1----------------------------------------------------
print("Hello")
print('Hello')
#Example2----------------------------------------------------
a = "Hello"
print(a)
#Example3----------------------------------------------------
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#Example4----------------------------------------------------
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
#Example5----------------------------------------------------
a = "Hello, World!"
print(a[1])
#Example6----------------------------------------------------
for x in "banana":
    print(x)
#Example7----------------------------------------------------
a = "Hello, World!"
print(len(a))
#Example8----------------------------------------------------
txt = "The best things in life are free!"
print("free" in txt)
#Example9----------------------------------------------------
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")
#Example10----------------------------------------------------
txt = "The best things in life are free!"
print("expensive" not in txt)
#Example11----------------------------------------------------
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")