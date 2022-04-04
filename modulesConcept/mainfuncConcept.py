from os import name
from pip import main


def printName(name):
    print(f"Good Morning, {name}!")

print(__name__) # when this will get called from test.py __name__ won't be main
if __name__ == '__main__': 
    name = input("Enter name: ")
    printName(name)