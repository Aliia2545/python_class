import change


def update():
    while True:
        try:
            data_for_update = input("Do you want to update something?\nEnter 1 for 'Yes'\nEnter 2 for 'No'\n")
            if data_for_update == "1":
                # print(registration.name_list, registration.age_list, registration.address_list)
                change.change()
            elif data_for_update == "2":
                print("Exit")
                break
            else:
                print("Something went wrong. Try again!")
        except ValueError:
            print("Enter the correct number!")
