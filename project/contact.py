import csv
from genericpath import exists # For excel

filename: str = 'file.csv'

def create_contact(name, number) -> bool:
    # FIrst check if name exists
    if contact_exists(name, number):
        return False
    with open(filename, 'a', encoding='utf8') as file:
        excel = csv.writer(file)
        excel.writerow([name, number])
        return True

def take_input(msg):
    while True:
        option = input(msg)
        if option.isnumeric:
            return int(option)
        continue

def send_msg() -> None:
    phone = input('Enter Number:')
    if contact_exists(number=phone):
        with open('msgs.csv', 'r', encoding='utf8') as file:
            writer = csv.writer(file)
            writer.writerow([phone, input('Enter MSG:')])

def list_contacts():
    try:
        with open(filename, 'r', encoding='utf8') as file:
            print('-----------------------')
            reader = csv.reader(file)
            for row in reader:
                print('Name=', row[0], ' Number=', row[1])
            print('-----------------------')
    except FileNotFoundError:
        print('Contacts not found')

def contact_exists(name="", number=""):
    try:
        with open(filename, 'r', encoding='utf8') as file:
            reader = csv.reader(file)
            for row in reader:
                if name != "" and name == row[0]:
                    return True
                if number != "" and number == row[1]:
                    return True
        return False
    except FileNotFoundError:
        init()
        return False

def init() -> None:
    with open(filename, 'w', encoding='utf8') as file:
        excel = csv.writer(file)
        excel.writerow(['Name' , 'telephone number', 'msg'])
