"""Contact Functions."""
import csv

filename: str = "file.csv"


def create_contact(name, number) -> bool:
    """Create contact."""
    # FIrst check if name exists
    if contact_exists(name, number):
        return False
    with open(filename, "a", encoding="utf8") as file:
        excel = csv.writer(file)
        excel.writerow([name, number])
        return True


def take_input(msg):
    """Responsible for taking input for options from user."""
    while True:
        option = input(msg)
        if option.isnumeric():
            return int(option)
        continue


def send_msg() -> bool:
    """Send msg to user."""
    phone = input("Enter Number:")
    if contact_exists(number=phone):
        with open("msgs.csv", "r", encoding="utf8") as file:
            writer = csv.writer(file)
            writer.writerow([phone, input("Enter MSG:")])
        return True
    return False


def list_contacts() -> None:
    """List all contacts from excel file."""
    try:
        with open(filename, "r", encoding="utf8") as file:
            print("-----------------------")
            reader = csv.reader(file)
            for row in reader:
                if len(row) > 0:
                    print("Name=", row[0], " Number=", row[1])
            print("-----------------------")
    except FileNotFoundError:
        print("Contacts not found")


def contact_exists(name="", number=""):
    """
    Check if contact exists or not.

    @param `name` (str) the name to check (defaults nothing)
    """
    if name == "" and number == "":
        Exception('No parameter found!')
    try:
        with open(filename, "r", encoding="utf8") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) > 0:
                    if name != "" and name == row[0]:
                        return True
                    if number != "" and number == row[1]:
                        return True
        return False
    except FileNotFoundError:
        init()
        return False


def init() -> None:
    """Create files."""
    with open(filename, "w", encoding="utf8") as file:
        excel = csv.writer(file)
        excel.writerow(["Name", "telephone number", "msg"])
    with open('msg.csv', "w", encoding="utf8") as file:
        excel = csv.writer(file)
        excel.writerow(["Telephone Number", "Msg"])
