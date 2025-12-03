import os

file_path = "test.txt"

with open(file_path, "r") as file:
    content = file.read()
    print(content)