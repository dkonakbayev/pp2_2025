class pers:
    def __init__(self,fname,lname):
        self.firstname = fname 
        self.lastname = lname
    def pri(self):
        print(self.firstname,self.lastname)
        
a = pers("Dau" , " Kon")
a.pri()