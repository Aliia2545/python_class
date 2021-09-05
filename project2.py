flights = {}
admins = {1111: "admin1", 2222: "admin2", 3333: "admin"}
passengers = {}
i = 0
while True:
    registration = input("Do you want to register? Choose '1'\nAre you an admin? Choose '2'\nExit '3'\n")
    if registration == "1":
        if len(flights) > 0:
            print(f"Exist flights: {flights}")
            choose_flight_code = input("Enter the flight code:").strip()
            if choose_flight_code.isdigit() and int(choose_flight_code) in flights:
                passengers_code = input("enter your passport ID(IDXXXX or ANXXXX):").strip()
                name = input("enter name: ").strip()
                age = input("enter age: ").strip()
                address = input("enter address: ").strip()
                phone_number = input("enter phone_number: ").strip()
                if ((str(passengers_code).startswith("ID") or str(passengers_code).startswith("AN") and len(passengers_code) > 5) and (len(name) > 2 and name.isalpha()) and (age.isdigit() and 1 < int(age) < 200) and len(address) > 3 and (
                        str(phone_number).startswith("0") and len(phone_number) == 10)):
                    passengers[passengers_code] = [name, age, address, phone_number, int(choose_flight_code)]
                    print("Congratulation! You have successfully registered!")
                else:
                    print("Something went wrong. Try again!")
            else:
                print("Enter the correct data!")
        else:
            print("There is no flights")
    elif registration == "2":
        admin_code = input("Enter the password of admin:").strip()
        if admin_code.isdigit() and admins.get(int(admin_code)):
            while True:
                register_flight = input("Do you want to register a flight?\nChoose 1 for 'Yes'\nChoose 2 for 'Passengers information'\nChoose 3 for 'Exit'\n").strip()
                if register_flight == "1":
                    city_from = input("enter the city from:").strip()
                    direction = input("enter the city to:").strip()
                    if (city_from.isalpha()) > 0 and (len(direction) > 3 and direction.isalpha()):
                        i += 1
                        flights[i] = [city_from, direction]
                        print(flights)
                    else:
                        print("Enter the correct data!")
                elif register_flight == "2":
                    if len(passengers) > 0:
                        print(passengers)
                    else:
                        print("There is no passengers registered")
                elif register_flight == "3":
                    print("Exit")
                    break
                else:
                    print("Something went wrong. Try again!")
        else:
            print("Something went wrong. Try again!")
    elif registration == "3":
        print("Exit")
        break
    else:
        print("Something went wrong. Enter the correct number")
