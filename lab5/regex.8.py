import re
str = input()
x = re.findall('[A-Z][^A-Z]*',str)
print(x)
