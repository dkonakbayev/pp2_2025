import re 
s = input()
a = r'^a(bb|bbb)$'

if re.fullmatch(a,s):
    print("match")
else:
    print("not match")