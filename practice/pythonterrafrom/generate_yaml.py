'''
step 1 - Add add arguments using argument parser
step 2 - Function to read jinja template
step 3 - Function to parse JSON
step 4 - Write file function to create file
'''
import argparse
import jinja2
import os
import sys
import json

def read_file(file):
    if os.path.exists(file):
        with open(file, 'r') as fr:
          data = fr.read()
          return data
    else:
        print(f"ERROR: file {file} doesn't exist!! Exiting!!!! ")
        sys.ext(1)

def parse_json(file):
    data = read_file(file)
    try:
        json_data = json.loads(data)
        return json_data
    except json.decoder.JSONDecodeError:
        print(f"ERROR : File {file} is not valid JSON")
        sys.exit(1)

def check_path(file):
    path_dir = "/".join(file.split('/')[:-1])
    if os.path.exists(path_dir):
        if os.path.exists(file):
          print('INFO : File {} already exists ! overwriting it !!! '.format(file))
    else:
        print('ERROR : Path {} doesnt exist .'.format(path_dir))
        sys.exit(1)
    
def write_file(file, data):
    with open(file, 'w') as fw:
        fw.write(data)

def read_jinja_template(template_file, template_path):
    templateLoader = jinja2.FileSystemLoader(searchpath=template_path)
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template(template_file)
    return template

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file",help="Location of input json",type=str,required=True)
    parser.add_argument("--template_location",help="template of the yaml",type=str,required=True)
    parser.add_argument("--output_file",help="Location of output file",type=str,required=True)
    args = parser.parse_args()
    input_file = args.input_file
    template = read_jinja_template("test.yaml",args.template_location)
    input_data = parse_json(input_file)
    outputText = template.render(input_data)
    write_file(args.output_file,outputText)

if __name__ == '__main__' :
    main()