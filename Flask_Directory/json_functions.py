import json

''' Using this script to read JSON files from the API so I can 
    analyze it and then pass and display the information '''


def read_from_file(filename):
    with open(filename, 'r') as read_file:
        data = json.load(read_file)
        return data


def save_to_file(data, filename):
    with open(filename, 'w') as write_file:
        json.dump(data, write_file, indent=2)
