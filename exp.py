import os

directory = 'C:\\Users\\Alihan\\PP2'
pathes = os.listdir(directory)

#Exercis1----------------------------------------------------
print("*list of directories*")
n=0
for path in pathes:
    if os.path.isdir(f"{directory}\\{path}"):
        n += 1
        print(f"{n}){path}")
n=0
print("*list of files and all directories*")
for path in pathes:
    n += 1
    print(f"{n}){path}")
n=0
print("*list of files*")
for path in pathes:
    if os.path.isfile(f"{directory}\\{path}"):
        n += 1
        print(f"{n}){path}")