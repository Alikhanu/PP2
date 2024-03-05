# Exercise 1 ----------------------------------------------------
import os

path = 'C:\\Users\\Alihan\\PP2'

# List only directories
print("Directories:")
for entry in os.listdir(path):
    if os.path.isdir(os.path.join(path, entry)):
        print(entry)

# List only files
print("\nFiles:")
for entry in os.listdir(path):
    if os.path.isfile(os.path.join(path, entry)):
        print(entry)

# List all directories and files
print("\nAll Directories and Files:")
for entry in os.listdir(path):
    print(entry)

# Exercise 2 ----------------------------------------------------
print("\nPath Accessibility:")
print("Existence:", os.path.exists(path))
print("Readability:", os.access(path, os.R_OK))
print("Writability:", os.access(path, os.W_OK))
print("Executability:", os.access(path, os.X_OK))

# Exercise 3 ----------------------------------------------------
print("\nPath Existence and File/Directory Extraction:")
if os.path.exists(path):
    filename = os.path.basename(path)
    directory = os.path.dirname(path)
    print("Filename:", filename)
    print("Directory:", directory)

# Exercise 4 ----------------------------------------------------
print("\nCounting the Number of Lines in a Text File:")
with open("file.txt", "r") as file:
    lines = file.readlines()
    print("Number of lines:", len(lines))

# Exercise 5 ----------------------------------------------------
print("\nWriting a List to a File:")
my_list = ["apple", "banana", "cherry"]
with open("list.txt", "w") as file:
    for item in my_list:
        file.write(item + "\n")

# Exercise 6 ----------------------------------------------------
print("\nGenerating Text Files A.txt to Z.txt:")
for char in range(ord('A'), ord('Z')+1):
    filename = f"{chr(char)}.txt"
    with open(filename, "w") as file:
        pass

# Exercise 7 ----------------------------------------------------
print("\nCopying Contents of a File to Another:")
with open("source.txt", "r") as source_file, open("destination.txt", "w") as destination_file:
    destination_file.write(source_file.read())

# Exercise 8 ----------------------------------------------------
print("\nDeleting a File by Specified Path:")
if os.path.exists("path there"):
    if os.access("path there", os.W_OK):
        os.remove("path there")
        print("File deleted successfully.")
    else:
        print("Permission denied to delete the file.")
else:
    print("The file does not exist.")