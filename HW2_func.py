
# problem1
# def func1(list):
#     print(list)
#     list1 = list[0:int(len(list)/2)]
#     list1.reverse()
#     list2 = list[int(len(list)/2): int(len(list))]
#     list2.reverse()
#
#     print(list1, list2)
# list_enter = [1, 3, 4, 5, 4, 7, 4, 3, 4, 9]
# func1(list_enter)

# problem2
# def func2():
#     a = 0
#     b = 1
#     for i in range(10):
#         c = a + b
#         a = b
#         b = c
#         c += b
#         print(c)
# func2()

# problem 3
# def subtraction(a, b):
#     c = a - b
#     return c
# def add(a, b):
#     d = a + b
#     return d
# def main():
#     a = 20
#     b = 10
#     c = subtraction(a, b)
#     d = add(a, b)
#     print(f"subtraction: {c}, addition: {d}")
# main()


# DAY2
# problem1

# a = 20
# b = 10
# def add(a, b):
#     c = a + b
#     return c
# def subtraction (a, b):
#     c = a - b
#     return c
# def multiply(a, b):
#     c = a * b
#     return c
# def divide(a, b):
#     c = a / b
#     return c
# c = add(a, b)
# print(c)
# d = subtraction(a, b)
# print(b)
# e = multiply(a, b)
# print(e)
# f = divide(a, b)
# print(f)


# problem2
# example = input("Enter: ")
# def func(sentence):
#     i = 0
#     for _ in sentence:
#         i+=1
#     return i
# c = func(example)
# print(c)


# probelm 3
# def func3(dictionary1, dictionary2):
#     dictionary1.update(dictionary2)
#     print(dictionary1)
# a = {1: "one", 2: "two"}
# b = {3: "three", 4: "four"}
# func3(a, b)
#
# def func4(*args):
#     print(args)
#     f = args[0]
#     k = args[1]
#     args[0].update(args[1])
#     print(args[0])
# func4(a, b)

# def func4(**kwargs):
#     print(kwargs)
#     kwargs["key1"].update(kwargs["key2"])
#     print(kwargs["key1"])
# func4(key1 = a, key2 = b)


# problem 1
# def func1():
#     def func2():
#         print("It's a second function")
#     print("It's a main function")
#     func2()
# func1()




# def fun8(**kwargs):
#     keys = []
#     items = []
#     d = list(kwargs["key"].items())
#     for i in d:
#         keys.append(i[0])
#         items.append(i[1])
#     keys = tuple(keys)
#     items = tuple(items)
#     return keys, items
#
#
# a = {1: 2, 4: 5}
# c = fun8(key=a)
# print(c[0], c[1], sep='|')


# problem 3
# def func7(number):
#     if number % 2 != 0 and number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
#         print("Simple number", number)
#     else:
#         print("Not simple number", number)
# func7(5)



def func9(a):
    x = 0
    for i in range(a+1):
        print(i)
        if a % i == 0:
            x += 1
        else:
            continue
        if x <= 2:
            return True
        else:
            return False
while True:
    a = 7
    if a > 0:
        ans = func9(a)
        if ans == True:
            print("Prostoe")
        else:
            print("Ne prostoe")
    else:
        print("error")