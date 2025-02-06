import random
s = input("Hello! What is your name? ")
print(f"Well, {s}, I am thinking of a number between 1 and 20.")

n = 0  
q = 1 
k = random.randint(1, 20) 

while n != k:
    print("Take a guess.")
    n = int(input())  
    
    if n == k:
        print(f"Good job, {s}! You guessed my number in {q} guesses!")
        break 
    elif n > k:
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")
    
    q += 1  