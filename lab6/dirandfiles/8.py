import os
path = str(input())

if os.path.exists(path):
    os.remove(path)
else:
    print("No such file exists.")