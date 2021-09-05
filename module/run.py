import registration


def main():
    while True:
        register = input("Enter 1 to register\nEnter 2 to exit\n")
        if register == "1":
            registration.registration_data()
        elif register == "2":
            print("Exit")
            break
        else:
            print("Something went wrong. Try again!")


if __name__ == '__main__':
    main()
