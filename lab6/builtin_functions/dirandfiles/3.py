def cheker(s) :
    s = s.lower()
    w = 0
    if (s == s[::-1]):
        w = "palindrome"
    else:
        w = "not palindrome" 
    return w
            
s = str(input())
print(cheker(s))

        