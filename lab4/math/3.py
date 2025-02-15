import math  

numb = int(input("number of sides: "))  
side = int(input("length of a side: "))  

S = (numb * side**2) / (4 * math.tan(math.pi / numb))  

print("The area of the polygon is:" ,S)  
