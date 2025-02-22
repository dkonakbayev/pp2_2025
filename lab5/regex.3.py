import re
s = input()
a = r'[a-z]+_[a-z]+$'
if re.fullmatch(a,s):
    print("found")
else:
    print("not found")