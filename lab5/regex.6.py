import re
s = input()
x = r'[ ,.]'
th=":"
newstring = re.sub(x,th,s)
print(newstring)