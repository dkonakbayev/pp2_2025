def check(a,b):
    for i in a:
        if not i in b:
            b.append(i)
    return b

a=input().split()
b=[]
print (check(a,b))