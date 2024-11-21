import os

# Name: read_file_name
# Parameters: None
# Return: f_name
# Processes user's input and output's if user's input is invalid
def read_file_name():
    f_name = input("Enter file name: ")
    while not os.path.isfile(f_name):
        f_name = input("File not exist. Enter file name: ")
    return f_name


def dictionary(f_name):
    mc_dict = {}
    for line in f_name:
        items  = line.split('\t')
        key = items[1]
        value = items[0]
        mc_dict[key] = value
    print(mc_dict)

def main(f_name):
    read_file_name()
    dictionary(f_name)


main('f_name')



