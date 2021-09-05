import registration


def check_data():
    print(registration.name_list, registration.age_list, registration.address_list)
    choose = input("Please, type the list to look at index via item!(age or address):").lower().strip()
    if choose == "age":
        print(registration.age_list)
        try:
            age_item = int(input("Enter your age:").strip())
            if age_item in registration.age_list:
                index_of_data = registration.age_list.index(age_item - 1)
                print(f"Index of your data is: {index_of_data}")
            else:
                print("There is no such age in list. Try again!")
        except ValueError:
            print("Enter your age with numbers!")
    elif choose == "address":
        print(registration.address_list)
        address = input("Enter your address:").strip()
        if len(address) > 3:
            if address in registration.address_list:
                index_of_address = registration.address_list.index(address)
                print(f"Index of your data is: {index_of_address}")
            else:
                print("Something went wrong. Try again!")
        else:
            print("Something went wrong. Try again!")

    else:
        print("Type the correct data!")
