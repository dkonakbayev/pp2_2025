def cheker(s):
    low = 0
    up = 0
    for i in s:
        if (i.islower()):
            low+=1 
        else:
            up+=1
    return f"Number of upper cases: {up}, Number of lower cases: {low}"     
s = str(input())
print(cheker(s))

        