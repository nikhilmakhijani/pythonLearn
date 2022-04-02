class Number:
    def __init__(self, num):
        self.num = num
    # Operator overloading
    def __add__(self, num2):
        print("adding the numbers")
        return self.num + num2.num
    
n1 = Number(4)
n2 = Number(5)
sum = n1 + n2
print("Sum is: "+str(sum))