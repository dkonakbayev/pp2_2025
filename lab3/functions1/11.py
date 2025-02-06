def check(s,i,j):
    if i>=j:
        return True
    if s[i]!=s[j]:
        return False
    return check(s,i+1,j-1)

s=str(input())
print("Yes")if check(s,0,len(s)-1)else print("No")