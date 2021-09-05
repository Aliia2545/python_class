import add_name
import add_age
# import add_address


from add_address import add_address as aa
def add():
    name_data = input("Please, type what do you want to change (name of list):")
    if name_data == "name":
        add_name.add_name()
    elif name_data == "age":
        add_age.add_age()
    elif name_data == "address":
        aa()
    else:
        print("Something went wrong. Try again!")
