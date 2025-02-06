def check (a,b,i,j):
    if j==len(b):
        return True
    if i==len(a):
        return False
    if a[i]==b[j]:
        return check(a,b,i+1, j+1)
    return check(a,b,i+1,j)

a=input().split()
b=["0", "0","7"]
print(check(a,b,0,0))