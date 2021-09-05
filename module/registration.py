import update

name_list = set()
age_list = []
address_list = []


def registration_data():
    try:
        name = input("Enter your name:")
        age = int(input("Enter your age:"))
        address = input("Enter your address:")
        if name.isalpha() and len(name) > 3 and 0 < age < 250 and len(address) > 3:
            name_list.add(name)
            age_list.append(age)
            address_list.append(address)
            print("You have successfully registered!")

            update.update()
        else:
            print("Something went wrong")
    except ValueError:
        print("Enter your data correctly!")
