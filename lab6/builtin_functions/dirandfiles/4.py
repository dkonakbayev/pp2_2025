from time import sleep
import math 
def square(n,m):
    sleep(m/1000)
    return math.sqrt(n) 

n = int(input())
m = int(input())
print("Square root of", n, "after", m, "miliseconds is", square(n, m))