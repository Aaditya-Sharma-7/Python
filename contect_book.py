#empty dictionary
contects = {
    
}

while True:
    print('\nContact Book App')
    print('1: Create contact')
    print('2: View contact')
    print('3: Update contact')
    print('4: Delete contact')
    print('5: Search contact')
    print('6: Count contact')
    print('7: Exit')

    choice = input('Enter Your choice = ')

    if choice == '1':
        name = input("Enter your name = ")
        if name in contects:
            print(f'Contect name {name} already exists!')

        else:
            age = input("Enter age = ")
            email = input("Enter email = ")
            mobile = input("Enter mobile = ")
            contects[name] = {'age':int(age), 'email':email, 'mobile':(mobile)}
            print(f'contect name {name} has been created successfully!')

    elif choice == '2':
        name = input("Enter contect to view = ")
        if name in contects:
            contect = contects[name]
            print(f'Name: {name}, Age:{contect["age"]}, Email:{contect["email"]}, Mibile Number:{contect["mobile"]}')
        else:
            print('contect not found!!')

    elif choice == '3':
        name = input('Enter name to update contact = ')
        if name in contects:
            age = input("Enter age = ")
            email = input("Enter email = ")
            mobile = input("Enter mobile = ")
            contects[name] = {'age':int(age), 'email':email, 'mobile':(mobile)}
        else:
            print('Name not found!')

    elif choice == '4':
        name = input('Enter contact name to delete = ')
        if name in contects:
            del contects[name]
            print(f'Contact name {name} has been deleted successfully')
        else:
            print('Contact not found!')

    elif choice == '5':
        search_name = input("Enter name you want to search = ")
        found = False
        for name, contect in contects.items():
            if search_name.lower() in name.lower():
                print(f'Found - Name {name}, Age:{age}, Email:{email}, Mobile Number:{mobile}')
                found = True
        if not found:
            print("No contact found with that name")

    elif choice == '6':
        print(f'Total contacts in your book : {len(contects)}')

    elif choice == '7':
        print("Goodbyy.....Program is closing....")
        break

    else:
        print("Invalid value")