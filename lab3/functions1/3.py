def solve(numheads,numlegs):
    rabbits = (numlegs - 2 * numheads) // 2
    chicken = numheads - rabbits 
    
    
    return rabbits , chicken 

nh = 35
nl = 94
print(solve(nh,nl))