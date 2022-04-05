
def tableGenerate(file, num):
    table = [ i*num for i in range(1,11) ]
    #print(table)
    writeFile(file, table)
            
def writeFile(file, data):
    with open(file , 'a') as f:
        f.write(str(data))
        f.write('\n')
    
def main():
    try:
       num = int(input("Enter the number: "))
       file = input("Enter file where you want to write: ")
       tableGenerate(file, num)
    except ValueError as e:
        print("Please enter a valid number")

if __name__ == '__main__':
    main()
