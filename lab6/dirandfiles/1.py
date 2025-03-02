import os

path = input()

print("Only directories:")
for name in os.listdir(path):
    if os.path.isdir(os.path.join(path, name)):  
        print(name)

print("\nOnly files:")
for name in os.listdir(path):
    if os.path.isfile(os.path.join(path, name)):  
        print(name)

print("\nAll directories and files:")
for name in os.listdir(path):
    print(name)
