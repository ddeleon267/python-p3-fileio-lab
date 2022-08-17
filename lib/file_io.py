import ipdb

def write_file(file_name, file_content):
    # ipdb.set_trace()
    with open(file_name + ".txt", mode='w', encoding='utf-8') as log_file: log_file.write(file_content)

def append_file(file_name, append_content):
    with open(file_name + ".txt", mode='a', encoding='utf-8') as log_file: log_file.write(append_content)


def read_file(file_name):
    with open(file_name + '.txt') as text_file:
        return text_file.read()


# Lets practice! In the file file_io.py write a function called write_file that takes in 
# the arguments file_name and file_content. The file_name can be a combined file path/name.
#  This function should use file_name and file_content to write a txt file.

# Write a append_to_file function that takes in the same parameters and appends to the .txt
#  file.

# Write a read_file function that takes in a file name and returns the content of the .txt 
# file.

