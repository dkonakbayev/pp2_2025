import os

path = str(input())
x = os.access(path, os.F_OK)
print('Exist:', x)

x = os.access(path, os.R_OK)
print('Readable:', x)

x = os.access(path, os.W_OK)
print('Writable:', x)

x = os.access(path, os.X_OK)
print('Executable:', x)