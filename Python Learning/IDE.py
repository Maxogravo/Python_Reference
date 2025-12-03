import os

filename = input("Filepath: ")

with open(filename, "w") as file:
    txt = input("Enter line of code: ")
    file.write(txt)