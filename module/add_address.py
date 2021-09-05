import registration


def add_address():
    add_address_to_list = input("Type your address to add: ")
    if len(add_address_to_list) > 3:
        try:
            method = int(input("How do you want to add?\n1 At the end\n2 By index:\n"))
            if method == 1:
                registration.address_list.append(add_address_to_list)
                print("Your address was successfully added")
            elif method == 2:
                index = int(input("Enter the index to add your address:"))
                if index <= len(registration.address_list):
                    registration.address_list.insert(index, add_address_to_list)
                    print("Your address was successfully added")
                else:
                    print("Index is out of the range of list")
            else:
                print("Something went wrong. Try again!")
        except Exception:
            print("Enter the number of index!")
