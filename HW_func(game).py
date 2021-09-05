i = 0
def game1(i):
    a = input("Enter the answer: 5 + 1 = ?\t").strip()
    if a == "6":
        i+=1
        a = input("Enter the answer: 20 * 2 = ?\t").strip()
        if a == "40":
            i+=1
            a = input("Enter the answer: 800 / 40 = ?\t").strip()
            if a == "20":
                i+=1
                a = input("Enter the answer: 20 % 2 = ?\t").strip()
                if a == "0":
                    i+=1
                    a = input("Enter the answer: 80 - 40= ?\t").strip()
                    if a == "40":
                        i+=1
                    else:
                        print("Your answer is not correct")
                else:
                    print("Your answer is not correct")
            else:
                print("Your answer is not correct")
        else:
            print("Your answer is not correct")
    else:
        print("Your answer is not correct")
    print(f"Your correct answer is: {i} question(s)")
    return i
def game2(i):

    b = input("'красный' in english (type):\t").lower().strip()
    if b == "red":
        i += 1
        b = input("'black' in russian(type):\t").lower().strip()
        if b == "черный":
            i+=1
            b = input("'room' in russian(type):\t").lower().strip()
            if b == "комната":
                i += 1
                b = input("'chandelier' in russian(type):\t").lower().strip()
                if b == "люстра":
                    i += 1
                    b = input("'kettle' in russian(type):\t").lower().strip()
                    if b == "чайник":
                        i += 1
                    else:
                        print("Your answer is not correct")
                else:
                    print("Your answer is not correct")
            else:
                print("Your answer is not correct")
        else:
            print("Your answer is not correct")
    else:
        print("Your answer is not correct")
    print(f"Your correct answer is: {i} question(s)")
    return i

def game3(i):

    b = input("World War 2 is stared in ____ year (enter the answer):\t").lower().strip()
    if b == "1939":
        i += 1
        b = input("First programming language is called (enter the name):\t").lower().strip()
        if b == "fortran":
            i += 1
            b = input("Macintosh was created by (enter the name):\t").lower().strip()
            if b == "steve jobs" or b == "jobs" or b == "steve":
                i += 1
                b = input("The biggest planet is (enter the name):\t").lower().strip()
                if b == "jupiter":
                    i += 1
                    b = input("Are you good person? (Yes, No):\t").lower().strip()
                    if b == "yes":
                        i += 1
                    else:
                        print("Your answer is not correct")
                else:
                    print("Your answer is not correct")
            else:
                print("Your answer is not correct")
        else:
            print("Your answer is not correct")
    else:
        print("Your answer is not correct")
    print(f"Your correct answer is: {i} question(s)")
    return i
while True:
    choose = input("Choose 1 to start the game1:\nChoose 2 to exit\t")
    if choose == "1":
        result_game1 = game1(i)
        if result_game1 > 3:
            game2(i)
            if i > 4:
                game3(i)
            else:
                print("Didn't enter")
        else:
            print("Didn't enter")
    elif choose == "2":
        print("exit")
        break
    else:
        print("Something went wrong. Try again!")


