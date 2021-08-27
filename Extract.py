import csv, os


#Creates a relative file path
filedir = os.path.dirname(os.path.realpath('__file__'))
csv_location = '2021-02-23-isle-of-wight.csv'
csv_path = os.path.join(filedir, csv_location)


#Extracts data from csv at path into dictionary
def extract_data(csv_path):
    contents = []
    with open(csv_path, 'r') as infile:
        fieldnames = ['Date_time','Location','Name','Products','Payment_type','Price','Card_Details']
        reader = csv.DictReader(infile, fieldnames = fieldnames)
        for row in reader:
            contents.append(row)
    return contents

Transaction_data = extract_data(csv_path)






