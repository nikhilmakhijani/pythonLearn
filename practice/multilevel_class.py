class Animal:
    def __init__(self):
        print("Animal class")

class Pets(Animal):
    def __init__(self):
        print("Pets class")

class Dog(Pets):
    def __init__(self):
        print("Dogs class")

    @staticmethod
    def bark():
       print("Bark")

def main():
     obj1 = Dog()
     obj1.bark()

if __name__ == '__main__':
    main()
    