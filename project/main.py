import contact

def main():
    while True:
        print('1 for list contancts', '2 for send msg', '3 for add','4 to exit' , sep="\n")
        option = contact.take_input('Enter Your Choice:')
        if option == 1:
            contact.list_contacts()
        elif option == 2:
            contact.send_msg()
        elif option == 3:
            ret = contact.create_contact(input('Enter Name:'), input('Enter Number:'))
            if ret == False:
                print('Name or phone Already Exists!')
        elif option == 4:
            break
main()
