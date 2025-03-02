def multiply(nums):
    mult = 1
    for x in nums:
        mult*=int(x)
    return mult 

nums = input().split()
print(multiply(nums))