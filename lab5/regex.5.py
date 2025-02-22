import re
s = input()
a = r'^a+[a-zA-Z]+b*$'
if re.fullmatch(a,s):
    print("found")
else:
    print("not found")
