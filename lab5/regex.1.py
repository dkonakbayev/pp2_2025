import re 
s = r'^a*b*$'
test = input()
if re.fullmatch(s,test):
    print("match")
else:
    print("not match")
