num = 24 # Global Num
def printNum():
    num = 7 # Local Num
    print(num)
# Function to show the use of global keyword
def printupdate():
    global num 
    num = 8
    print(num)

print(num) # Prints Global num value = 24
printNum() # Prints Local num value = 7
printupdate() # This updates global variable value to 7
print(num) # This confirms the update of global variable 

