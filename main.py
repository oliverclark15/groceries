import receipt_functions
import sys


def main():
    if sys.argv[1] == 'add':
        file_name = sys.argv[2]
        r1 = receipt_functions.read_in_receipt(file_name)
        receipt_functions.print_receipt(r1)
    else: print('invalid argument(s).')

main()