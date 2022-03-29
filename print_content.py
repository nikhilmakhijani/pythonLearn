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

def print_content(file):
    check_path(file)
    with open(file, 'r') as fl:
      data = fl.read()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input',help="input line",type=str,required=True)
    args = parser.parse_args()
    input_data= args.input
    print_content(input_data) 

if __name__=='__main__':
    main()
