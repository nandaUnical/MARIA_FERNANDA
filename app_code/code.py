#Application to work with word frecuencies in a collection of .txt files

import os

path = 'C:\Users\hp\Documents\!Master\Agile\!!Second Apello\ejemplos' 

def read_text (text_path):
    #If the input is a list of .txt files put all the text into a single dicc
    #If the input is a folder path read all the .txt files and put all the text into a single dicc
    #Return a dicc

    files_words_frecuency = {}
    files_content = []

    if type(text_path) == 'str':  
        for filename in filter(lambda p: p.endswith("txt"), os.listdir(text_path)):
            filepath = os.path.join(text_path, filename)
            with open(filepath, mode='r') as f:
                files_content += [f.read()]
    elif type(text_path) == 'list':
        for filename in text_path :
            with open(filename, mode='r') as f:
                files_content += [f.read()]

    for i in files_content:
        if i.lower() in files_words_frecuency:
            files_words_frecuency[i.lower()] += 1
        else:
            files_words_frecuency[i.lower()] = 1

    return files_words_frecuency


'''
import glob

for filename in glob.glob('*txt'):
    print(filename)




import os
import glob

folder_path = '/path/to/folder/containing/text/files'

# Use glob to find all the text files in the folder


# Loop through each file and read its contents
for file_path in files:
    with open(file_path, 'r') as file:
        contents = file.read()
        print(contents)

files = glob.glob(os.path.join(text_path, '*.txt'))

'''