# from registration import name_list, age_list, address_list
import registration


def delete():
    name_data = input("Please, type what do you want to change (name of list):")
    if name_data == "name":
        print(registration.name_list)
        delete_name = input("Type the name to delete:")
        if delete_name in registration.name_list:
            registration.name_list.remove(delete_name)
            print("You deleted the name")
        else:
            print("There is no such a name in name list")
    elif name_data == "age":
        print(registration.age_list)
        try:
            method = int(input("How do you want to delete?\n1 via item\n2 via index:\n"))
            if method == 1:
                delete_age = input("Type the age to delete:")
                if delete_age in registration.age_list:
                    registration.age_list.remove(delete_age)
                    print("You deleted the age")
                else:
                    print("There is no such an age in age list")
            elif method == 2:
                try:
                    index = int(input("Enter the index of item:"))
                    if index <= len(registration.age_list):
                        registration.age_list.pop(index)
                        print("You deleted the age")
                    else:
                        print("Index is out of the range of list")
                except Exception:
                    print("Enter the number of index")
            else:
                print("Something went wrong. Try again!")
        except Exception:
            print("Choose the number!")
    elif name_data == "address":
        print(registration.address_list)
        try:
            method = int(input("How do you want to delete?\n1 via item\n2via index:\n"))
            if method == 1:
                delete_address = input("Type the address to delete:")
                if delete_address in registration.address_list:
                    registration.address_list.remove(delete_address)
                    print("You deleted the address")
                else:
                    print("There is no such an address in address list")
            elif method == 2:
                try:
                    index = int(input("Enter the index of item:"))
                    if index <= len(registration.address_list):
                        registration.address_list.pop(index)
                        print("You deleted the address")
                    else:
                        print("Index is out of the range of list")
                except Exception:
                    print("Enter the number of index")
            else:
                print("Something went wrong. Try again!")
        except Exception:
            print("Choose the number!")
    else:
        print("Something went wrong. Try again!")
