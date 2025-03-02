list = input().split(' ')

with open("c:/Users/Daulet/Desktop/pp2/lab6/dirandfiles/file.txt", "w") as file:
        for c in list:
                file.write("%s\n" % c)

x = open("c:/Users/Daulet/Desktop/pp2/lab6/dirandfiles/file.txt")
print(x.read())