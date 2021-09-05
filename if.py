'''name = 'alexx'
code = 600
if name == 'alex' and code == 234:
    print("agent")

else:
    print("no")
print('welcome')
'''
'''
USD = 80
EURO = 90
money = int(input("Amount of money you want to exchange:"))
currency = int(input("Code of currency (USD=400, EURO= 401: )"))
if currency == 400:
    cash = round(money / USD)
    print("Your money:", cash, "dollar")
elif currency == 401:
    cash = round(money / EURO)
    print("Your  money:", cash, "euro")
else:
    cash = 0
    print("unknown currency", cash)
print("end", cash)
'''

name = 'Tom'
age = 22
Korean = False
if age >= 17 and Korean:
    student = "local_undergraduated_student"
    print(name, student)
elif 22 <= age <= 24 and Korean:
    student = "local_graduated_student"
    print(name, student)
elif age >= 25 and Korean:
    student = "local_PhD_student"
    print(name, student)
elif age >= 17 and not Korean:
    student = "international_undergraduated_student"
    print(name, student)
elif 22 <= age <= 24 and not Korean:
    student = "international_graduated_student"
    print(name, student)
elif age >= 25 and not Korean:
    student = "international_PhD_student"
    print(name, student)
else:
    print("Not student")

