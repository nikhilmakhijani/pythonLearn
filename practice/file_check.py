import os

def check_path(file):
    path_dir = "/".join(file.split('/')[:-1])
    if os.path.exists(path_dir):
         if os.path.exists(file):
             print("File {} exists".format(file))
             return 0
         else:
             return 1
    else:
        return 1


def read_file(file):
      if check_path(file) == 0:
         with open(file, 'r') as fr:
          print(fr.read())
      else:
         print("File {} doesn't exist".format(file))

def main():
    file1 = input("Enter file path: ")
    read_file(file1)

if __name__ == '__main__':
    main()
