def check(a):
    for i in range(len(a)-1):
        if a[i]=="3" and a[i+1]==3:
            return "Yes"
        return "No"
    
a=input().split()
print(check(a))