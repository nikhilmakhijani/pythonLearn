from decimal import DivisionByZero
import sys
 
while(True):
 num1 = input("Enter your number or q to exit: ")
 if num1 == 'q' or num1 == 'Q':
     break
 else:
  try:
   result = 100/int(num1)
   print("your result is: "+str(result))
  except ValueError as e:
   print("Please provide an integer")
   sys.exit(1)
  except DivisionByZero as e:
   print("You can not divide by zero")
  finally:                     # It will get executed no matter what even though we are exiting the code 
       print("We are done")

print("thanks for trying")
