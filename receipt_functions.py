import csv
import groc
import receipt


def read_in_receipt():
    file_name = input("Provide CSV file name: ")
    f = open(file_name, 'r')
    reader = csv.reader(f)
    print("Parsing through " + file_name + '...')
    groc_list = {}
    for row in reader:
        new_groc = groc.Groc(row[0], row[1], row[2])
        groc_list[new_groc.get_name()] = (row[1], row[2])
    f.close()
    new_receipt = receipt.Receipt(groc_list)
    return new_receipt

def print_receipt(receipt):
    print(receipt.get_groc_list())

r1 = read_in_receipt()

print_receipt(r1)
