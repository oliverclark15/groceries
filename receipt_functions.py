import csv
import groc
import receipt


def read_in_receipt(file_name):
    f = open(file_name, 'r')
    reader = csv.reader(f)
    groc_list = {}
    for row in reader:
        new_groc = groc.Groc(filter_name(row[0]), filter_mass(row[1]), (row[2]))
        groc_list[new_groc.get_name()] = (new_groc.get_mass(), new_groc.get_price())
    f.close()
    new_receipt = receipt.Receipt(groc_list)
    return new_receipt


def filter_mass(groc_mass):
    return groc_mass.split('g')[0]


def filter_price(groc_price):
    return groc_price.split('$')[1]


def filter_name(groc_name):
    if ': ' in groc_name:
        groc_name = groc_name.split(': ')[1]
    if ' [' in groc_name:
        groc_name = groc_name.split(' [')[0]
    if  ' (' in groc_name:
        groc_name = groc_name.split(' (')[0]

    return groc_name


def print_receipt(receipt):
    print(receipt.get_groc_list())