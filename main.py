import os

# Name: read_file_name
# Parameters: None
# Return: f_name
# Processes user's input and output's if user's input is invalid


def dictionary(filename):
    morse_dictionary = {}
    morse_data = open(filename, 'r')
    for line in morse_data:
        items = line.split('  ')
        key = items[1].strip()
        value = items[0].split()
        morse_dictionary[key] = value
    morse_data.close()
    return morse_dictionary

def main():
    print(dictionary('mc_dict.txt'))
main()





