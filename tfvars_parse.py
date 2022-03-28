'''
1) Take two inputs a) tfvars to convert b) location of output file
2) Check if file path exists then if file exists
3) function to parse to JSON
4) function to write 
'''
import os
import argparse
import sys
import hcl 
import json

# Function to check file path 
def check_path(file):
    path_dir = '/'.join(file.split('/')[:-1])
    # print( "inside check_path")
    if os.path.exists(path_dir):
       if os.path.exists(file):
          print("INFO : file {} already exists!! overwriting it".format(file))
    else:
        print("Error : Path {} doesnt exist".format(path_dir))
        sys.exit(1)

# Function to write data
def write_file(file,data):
    check_path(file)
    with open(file,'w') as fl:
        fl.write(data)

# Function to convert to json 
def write_json_file(file,data):
    jsondata=json.dumps(data,indent=2)
    write_file(file,jsondata)

# Funtuon to convert from tfvars to json format
def parse_tfvars(file):
    #  print("inside parse function")
     check_path(file)
     with open(file, 'r') as fp:
         obj = hcl.load(fp)
     return obj


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file",help="Location of terraform.tfvars file",
                        type=str,required=True)
    parser.add_argument("--output_file",help="Location to store JSON output file",
                        type=str,required=True)
    args = parser.parse_args()
    input_file = args.input_file
    output_file = args.output_file
    input_data = parse_tfvars(input_file)
    write_json_file(output_file,input_data)

if __name__ == '__main__' :
    main()

