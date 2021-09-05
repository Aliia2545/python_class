import registration


def add_age():
    try:
        add_age_to_list = int(input("Type an age to add:"))
        if 0 < add_age_to_list < 250:
            try:
                method = int(input("How do you want to add?\n1 At the end\n2 By index:\n"))
                if method == 1:
                    registration.age_list.append(add_age_to_list)
                    print("Your age was successfully added")
                elif method == 2:
                    try:
                        index = int(input("Enter the index to add your age:"))
                        if index <= len(registration.age_list):
                            registration.age_list.insert(index, add_age_to_list)
                            print("Your age was successfully added")
                        else:
                            print("Index is out of the range of list")
                    except Exception:
                        print("Enter index as number!")
                else:
                    print("Something went wrong. Try again!")
            except Exception:
                print("Choose the number")
        else:
            print("Something went wrong. Try again!")
    except Exception:
        print("Enter the number")
