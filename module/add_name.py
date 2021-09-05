import registration


# from registration import name_list
def add_name():
    add_name_to_list = input("Type a name to add:")
    if add_name_to_list.isalpha and len(add_name_to_list) > 3:
        registration.name_list.add(add_name_to_list)
        # name_list.add(add_name_to_list)
        print("Name was successfully added")
    else:
        print("Something went wrong. Try again!")
