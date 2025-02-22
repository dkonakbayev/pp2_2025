import re 
s = input()
a = r'^[A-Z]+[a-z]+$'
if re.fullmatch(a,s):
    print("sequence is found")
else:
    print("sequence is not found")

        
    