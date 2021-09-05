# my_list = [1, 'Mario', 3.5]
# def length():
#     res = 0
#     for _ in range(my_list):
#         res += 1
#     print(res)
#
# def hello():
#     print("Hi")
# def goodbye():
#     print("Goodbye")
# while True:
#     ac = input('input 1 or 2')
#     if ac == "1":
#         hello()
#         print("Hi")
#     elif ac == "2":
#         goodbye()
#         break
#     else:
#         print("Error")
# def say_hello(name="user"):
#     print("salam aleikum", name)
#
# def say_goodbye(name):
#     print("goodbye", name)
#
# naame = input("Enter a name:")
# say_hello("baktybek")
# say_goodbye(naame)

# def data(age, name, lastname="user_name"):
#     print(name)
#     print(lastname)
#     print(age)
#
# data("Aliia", "Beish", 23)
# data( name="Artur", age=20, lastname="Akimov")
# data(name="Aisel", age=23)
# data(23, "name")


def exchange(usd_rate, money):
    result = round(money / usd_rate, 2)
    return result


result1 = exchange(60, 30000)
print(result1)
result2 = exchange(56, 30000)
print(result2)
result3 = exchange(65, 30000)
print(result3)
