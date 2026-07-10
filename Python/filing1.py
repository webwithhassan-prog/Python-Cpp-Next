# open a file
# read/write/append
# calling function
# close a file


import os

filename = "cal.py"
if not os.path.exists(filename):
    print(f" {filename} file not found!")
else:
    file = open(filename, "w")
    file.write("My name is Tosiq")
    file.close()

def showText():
    file = open(filename, "r")
    content = file.read()
    print(f"Content: {content}")
    file.close()

showText()

# with open('filing1.txt', "r") as file:
#     print(f" File with keyword: {file.open()}")


