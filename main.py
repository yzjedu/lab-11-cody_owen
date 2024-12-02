import os

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

def translate_morse(translation, input, output):
    morse_dict = dictionary(translation)
    with open(input, 'r') as file:
        morse_lines = file.readlines()
    t_lines = []
    for line in morse_lines:
        translated_words = []
        for words in line.strip().split(' '):

            word = ''.join(morse_dict[letter][0]
            for letter in words.split())
            translated_words.append(word)

        t_lines.append(''.join(translated_words))

    with open(output, 'w') as outfile:
        outfile.write('\n'.join(t_lines) + '\n')


def read_file_name():
    f_name = input("Enter file name, (first is to translate dictionary, second is to translate a file): ")
    while not os.path.isfile(f_name):
        f_name = input("File not exist. Enter file name: ")
    return f_name



def main():
    conversion_file = read_file_name()
    input_file = read_file_name()
    output_file = input("Enter the name of the output file: ")
    translate_morse(conversion_file, input_file, output_file)

main()
