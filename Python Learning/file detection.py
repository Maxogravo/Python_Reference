#File detection
import os

file_path = "test.txt" #Relative file path

if os.path.exists(file_path):
    print("true")
else:
    print("False")