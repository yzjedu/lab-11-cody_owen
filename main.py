# Programmers:  Owen & Cody
# Course:  CS151, Dr. Yalew
# Due Date: 12/2
# Programming Assignment:  Lab 11
# Problem Statement: translates morsecode to english, then reads files in morsecode and translates to a different file
# Data In: file names
# Data Out:  morsecode translations
# Credits: class reference for dictionary function, notes


import os

# Name: dictionary
# Parameters: filename
# Return: morse_dictionary
# translates morsecode to english
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

# Name: translate_morse
# Parameters: translation, input, output
# Return: none
# translate each word in file, stores in a list, then outputs each word on its own line in a file, name chosen by user
def translate_morse(translation, input, output):
    #calls the dictionary
    morse_dict = dictionary(translation)
    #open file for reading
    with open(input, 'r') as file:
        morse_lines = file.readlines()
    t_lines = []
    #stores each word in the list
    for line in morse_lines:
        translated_words = []
        for words in line.strip().split(' '):
            #joins each letter into the word it is s apart of
            word = ''.join(morse_dict[letter][0]
            for letter in words.split())
            translated_words.append(word)

        t_lines.append(''.join(translated_words))

    with open(output, 'w') as outfile:
        outfile.write('\n'.join(t_lines) + '\n')

# Name: read_file_name
# Parameters: None
# Return: f_name
# Processes user's input and output's if user's input is invalid
def read_file_name():
    f_name = input("Enter file name, (first is to translate dictionary, second is to translate a file): ")
    while not os.path.isfile(f_name):
        f_name = input("File not exist. Enter file name: ")
    return f_name


# Name: main
# Parameters: None
# Return: none
# runs the main function
def main():
    conversion_file = read_file_name()
    input_file = read_file_name()
    output_file = input("Enter the name of the output file: ")
    translate_morse(conversion_file, input_file, output_file)

#calls main
main()
