# user str
# class str
# function: palindrome
# min 3

class Pal:
    def __init__(self, s):
        self.s = s.lower()
    
    def ispolindrome(self):
        if self.s == self.s[::-1]:
            print("palindrome")
        else:
            print("not palindrome")

s = input()
pal_checker = Pal(s)
pal_checker.ispolindrome()

        
            
        
        
