import argparse
import os
import sys

def check_path(file):
    path_dir = '/'.join(file.split('/')[:-1])
    if os.path.exists(path_dir):
        if os.path.exists(file):
            print("file {} exists".format(file))
    else:
        print("file {} doesnt exist".format(file))
        sys.exit(1)

def print_content(file,word):
    check_path(file)
    with open(file, 'r') as fl:
     if word in fl.read():
         print ("Yes, word - {} exists".format(word))
     else:
         print( "word - {} not found".format(word))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input',help="input line",type=str,required=True)
    args = parser.parse_args()
    input_data= args.input
    word = input("Enter the word you want to search: ")
    print_content(input_data,word) 

if __name__=='__main__':
    main()
