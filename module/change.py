import add
import delete
import check_data


def change():
    try:
        choose_change = int(input("Enter 1 to add\nEnter 2 to delete\nEnter 3 to check your data\nEnter 4 to exit\t"))
        if choose_change == 1:
            add.add()
        elif choose_change == 2:
            delete.delete()
        elif choose_change == 3:
            check_data.check_data()
        elif choose_change == 4:
            print("Exit")
            return 0
        else:
            print("Something went wrong. Try again!")
    except Exception:
        print("Choose the correct number!", Exception)
