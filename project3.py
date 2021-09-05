name_list = set()
age_list = []
address_list = []
phone_number_list = set()
while True:
    command_1 = input("1 is Registration\n2 is Exit\n").strip()
    if command_1 == "1":
        name = input("enter name: ").strip()
        age = input("enter age: ").strip()
        address = input("enter address: ").strip()
        phone_number = input("enter phone_number: ").strip()
        if (len(name) > 2 and name.isalpha()) and (age.isdigit() and 1 < int(age) < 200) and len(address) > 5 and (
                str(phone_number).startswith("0") and len(phone_number) == 10):
            name_list.add(name)
            age_list.append(age)
            address_list.append(address)
            phone_number_list.add(phone_number)
            print(name_list, age_list, address_list, phone_number_list)
            while True:
                add = input("Do you want to upgrade?\n1 is YES\n2 is NO\n")
                if add == "1":
                    choose = input(
                        "Please, select an operation:\n1 is Add data\n2 is Delete data\n3 is Know the index of your data\n4 is Know the amount of items\n5 is Look at the lists(sort)\n")
                    if choose == "1":
                        add_data = input("What do you want to add? Please, type the list name!").lower().strip()
                        if add_data == "name":
                            name = input("enter name:").strip()
                            if len(name) > 2 and name.isalpha() :
                                if name in name_list:
                                    print("This name is already exist!")
                                else:
                                    name_list.add(name)
                                    print(name_list, age_list, address_list, phone_number_list)
                            else:
                                print("Something went wrong. Enter the correct data!")
                        elif add_data == "age":
                            age = input("enter age: ").strip()
                            if age.isdigit() and 1 < int(age) < 200:
                                ask_how_to_add = input(
                                    "How do you want to add?\n1 is At the end\n2 is By index\n").strip()
                                if ask_how_to_add == "1":
                                    age_list.append(age)
                                    print(name_list, age_list, address_list, phone_number_list)
                                elif ask_how_to_add == "2":
                                    ask_number_of_index = int(input("enter an index:").strip())
                                    if ask_number_of_index in range(len(age_list)):
                                        age_list.insert(ask_number_of_index, age)
                                        print(name_list, age_list, address_list, phone_number_list)
                                    else:
                                        print("Something went wrong. Enter the correct data!")
                                else:
                                    print("Error")
                            else:
                                print("Something went wrong. Enter the correct data!")
                        elif add_data == "address":
                            address = input("enter address: ").strip()
                            if len(address) > 5:
                                ask_how_to_add = input(
                                    "How do you want to add?\n1 is At the end\n2 is By index\n").strip()
                                if ask_how_to_add == "1":
                                    address_list.append(address)
                                    print(name_list, age_list, address_list, phone_number_list)
                                elif ask_how_to_add == "2":
                                    ask_number_of_index = int(input("enter an index:").strip())
                                    if ask_number_of_index in range(len(address_list)):
                                        address_list.insert(ask_number_of_index, address)
                                        print(name_list, age_list, address_list, phone_number_list)
                                    else:
                                        print("Something went wrong. Enter the correct data!")
                                else:
                                    print("Error")
                            else:
                                print("Something went wrong. Enter the correct data!")
                        elif add_data == "phone number" or add_data == "phonenumber" or add_data == "phone_number" or add_data == "number":
                            phone_number = input("enter phone_number: ").strip()
                            if str(phone_number).startswith("0") and len(phone_number) == 10:
                                phone_number_list.add(phone_number)
                                print(name_list, age_list, address_list, phone_number_list)
                            else:
                                print("Something went wrong. Enter the correct data!")
                        else:
                            print("Error")
                    elif choose == "2":
                        ask_for_delete = input("Do you want to delete something?\n1 is YES\n2 is NO\n").strip()
                        if ask_for_delete == "1":
                            delete_data = input(
                                "What do you want to delete? Please, type the list name!\n").lower().strip()
                            if delete_data == "name":
                                ask_how_to_delete = input(
                                    "How do you want to delete?\n1 is Delete an item\n2  is Delete everything\n").strip()
                                if ask_how_to_delete == "1":
                                    print(name_list)
                                    ask_an_item = input("Enter the name\n").strip()
                                    if ask_an_item in name_list:
                                        name_list.remove(ask_an_item)
                                        print(name_list, age_list, address_list, phone_number_list)
                                    else:
                                        print("There is no such a data. Please, enter the correct data!")

                                elif ask_how_to_delete == "3":
                                    name_list.clear()
                                    print(name_list, age_list, address_list, phone_number_list)
                                else:
                                    print("Error")
                            elif delete_data == "age":
                                ask_how_to_delete = input(
                                    "How do you want to delete?\n1 is Delete an item\n2 is Delete by index\n3 is Delete everything\n").strip()
                                if ask_how_to_delete == "1":
                                    print(age_list)
                                    ask_an_item = input("Enter the age\n").strip()
                                    if ask_an_item in age_list:
                                        age_list.remove(ask_an_item)
                                        print(name_list, age_list, address_list, phone_number_list)
                                    print("There is no such an data")
                                elif ask_how_to_delete == "2":
                                    print(age_list)
                                    ask_an_index = int(input("Enter the index of the age\n"))
                                    if ask_an_index in range(len(age_list)):
                                        age_list.pop(ask_an_index)
                                        print(name_list, age_list, address_list, phone_number_list)
                                    print("Something went wrong. Enter the correct data!")
                                elif ask_how_to_delete == "3":
                                    age_list.clear()
                                    print(name_list, age_list, address_list, phone_number_list)
                                else:
                                    print("Error")
                            elif delete_data == "address":
                                ask_how_to_delete = input(
                                    "How do you want to delete?\n1 is Delete an item\n2 is Delete by index\n3 is Delete everything\n").strip()
                                if ask_how_to_delete == "1":
                                    print(address_list)
                                    ask_an_item = input("Enter the address\n").strip()
                                    if ask_an_item in address_list:
                                        address_list.remove(ask_an_item)
                                        print(name_list, age_list, address_list, phone_number_list)
                                    else:
                                        print("Something went wrong. Enter the correct data!")
                                elif ask_how_to_delete == "2":
                                    print(address_list)
                                    ask_an_index = int(input("Enter the index of the address\n"))
                                    if ask_an_index in range(len(address_list)):
                                        address_list.pop(ask_an_index)
                                        print(name_list, age_list, address_list, phone_number_list)
                                    else:
                                        print("Something went wrong. Enter the correct data!")
                                elif ask_how_to_delete == "3":
                                    address_list.clear()
                                    print(name_list, age_list, address_list, phone_number_list)
                                else:
                                    print("Error")
                            elif delete_data == "phone number" or delete_data == "phonenumber" or delete_data == "phone_number" or delete_data == "number":
                                ask_how_to_delete = input(
                                    "How do you want to delete?\n1 is Delete an item\n2 is Delete everything\n").strip()
                                if ask_how_to_delete == "1":
                                    print(phone_number_list)
                                    ask_an_item = input("Enter the phone number\n").strip()
                                    if ask_an_item in phone_number_list:
                                        phone_number_list.remove(ask_an_item)
                                        print(name_list, age_list, address_list, phone_number_list)
                                    else:
                                        print("Something went wrong. Enter the correct data!")
                                elif ask_how_to_delete == "3":
                                    phone_number_list.clear()
                                    print(name_list, age_list, address_list, phone_number_list)
                                else:
                                    print("Error")
                            else:
                                print("Error")
                        elif ask_for_delete == "2":
                            continue
                        else:
                            print("Error")
                    elif choose == "3":
                        list_of_items = input("Please, type the list name!\n").lower().strip()

                        if list_of_items == "age":
                            print(age_list)
                            item_of_index = input("Enter the age\n").strip()
                            print(age_list.index(item_of_index))
                        elif list_of_items == "address":
                            print(address_list)
                            item_of_index = input("Enter the address\n").strip()
                            print(address_list.index(item_of_index))
                        else:
                            print("Error")
                    elif choose == "4":
                        list_of_items = input("Please, type the list name!\n").lower().strip()
                        if list_of_items == "name":
                            print(name_list)
                            print("list name contains " + str(len(name_list)) + " element(s)")
                        elif list_of_items == "age":
                            print(age_list)
                            print("list age contains " + str(len(age_list)) + " element(s)")
                        elif list_of_items == "address":
                            print(address_list)
                            print("list address contains " + str(len(address_list)) + " element(s)")
                        elif list_of_items == "phone number" or list_of_items == "phonenumber" or list_of_items == "phone_number" or list_of_items == "number":
                            print(phone_number_list)
                            print("list phone number contains " + str(len(phone_number_list)) + " element(s)")
                        else:
                            print("Error")
                    elif choose == "5":
                        list_of_items = input("Please, type the list name!\n").lower().strip()

                        if list_of_items == "age":
                            choose_sort = input(
                                "Choose the method of sort\n1 is sorting by increasing\n2 is sorting by decreasing\n")
                            if choose_sort == "1":
                                age_list.sort()
                                print(age_list)
                            elif choose_sort == "2":
                                age_list.sort()
                                age_list.reverse()
                                print(age_list)
                            else:
                                print("Error")
                        elif list_of_items == "address":
                            choose_sort = input(
                                "Choose the method of sort\n1 is sorting by increasing\n2 is sorting by decreasing\n")
                            if choose_sort == "1":
                                address_list.sort()
                                print(address_list)
                            elif choose_sort == "2":
                                address_list.sort()
                                address_list.reverse()
                                print(address_list)
                            else:
                                print("Error")

                        else:
                            print("Error")
                    else:
                        print("Error")
                elif add == "2":
                    break
                else:
                    print("Error")
        else:
            print("Something went wrong. Enter the correct data!")
    elif command_1 == "2":
        print("Exit from program")
        break
    else:
        print("Error")
