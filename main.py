#!/usr/local/bin/python3

import sys
from Field import Field
from Spec import Spec

specPath = "MARCspec.json"

def main(mrc_path):
    with open(mrc_path, newline='') as file:
        data = file.read()
        lint_record(data)
#TODO        multiline for MARCrecord in data: #MARC files must be separated by newlines

def split_directory_into_fields(directory):
    working_directory = directory
    directory_entries = list()

    while len(working_directory) >= 12:
        directory_entries.append(working_directory[0:11])
        working_directory = working_directory[12:]

    #If the segmentation left an uneven set of twelve, this content directory string was malformed
    if (len(working_directory)!= 0):
        raise ValueError("There are not the right number of digits in the content directory")

    return directory_entries

def lint_record(record):
    spec = Spec(specPath)

    leader = record[0:23]
    directory = record[24:].split('\x1e1')[0]
    content = record[24:].split('\x1e1',1)[1]

    try:
        directory_entries = split_directory_into_fields(directory)
    except ValueError:
        raise

    for field_metadata in directory_entries:
        field = Field(field_metadata, content, spec)
        print(field.tag, field.content)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print("Be sure you include the relative path to the marc file input")
