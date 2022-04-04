while(True):
    value = input("Enter the number or Press 'q' to exit: ")
    if value == 'q' or value == 'Q':
        break
    try:
      if int(value) > 6:
        print("{} is greater than 6".format(value))
      else:
        print("{} is less than 6".format(value))
    except Exception as e:
        print(f"You need to give an integer. Error is:{e} ")
