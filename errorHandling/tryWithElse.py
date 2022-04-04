import sys
 
while(True):
 num1 = input("Enter your number or q to exit: ")
 if num1 == 'q' or num1 == 'Q':
     break
 else:
  try:
   result = 100/int(num1)
  except ValueError as e:
   print("Please provide an integer")
  except ZeroDivisionError as e:
   print("You can not divide by zero")
  else:
    print("We were successful")
    print("your result is: "+str(result))
