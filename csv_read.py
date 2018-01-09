import csv


def read_in():
    invoice_file = input("Provide CSV file name: ")
    print("Parsing through " + invoice_file)
    f = open(invoice_file, 'r')
    reader = csv.reader(f)
    product_names = []
    product_weights = []
    product_price = []
    for row in reader:
        product_names.append(row[0])
        print (row[0])
        temp1 = row[1]
        # temp1.replace('g','')
        product_weights.append(temp1)
        print (temp1)
        temp2 = row[2]
        # temp2.replace('$','')
        product_price.append(temp2)
        print (temp2)
    f.close()

read_in()