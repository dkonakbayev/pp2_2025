import string
import os

for letter in string.ascii_uppercase:
    x = letter + ".txt"
    with open("c:/Users/Daulet/Desktop/pp2/lab6/dirandfiles/file.txt" + x, "w") as file:
       file.writelines(letter)