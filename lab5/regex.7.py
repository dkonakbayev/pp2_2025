import re

s = str(input())

x = re.sub("_", " ", s)

x = x.title()

x = re.sub("\s", "", x)

print(x)