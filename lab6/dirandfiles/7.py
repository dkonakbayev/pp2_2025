with open("c:/Users/Daulet/Desktop/pp2/lab6/dirandfiles/file.txt") as file:
    with open("c:/Users/Daulet/Desktop/pp2/lab6/dirandfiles/copy.txt", "w") as file1:
        for line in file:
            file1.write(line)