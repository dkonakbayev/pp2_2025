def check(a, i, j):
    if i == len(a):
        return
    if j == int(a[i]):
        print()
        return check(a, i + 1, 0)
    print("*", end="")
    return check(a, i, j + 1)

a = input().split()
check(a, 0, 0)