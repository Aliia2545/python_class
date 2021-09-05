# def new(a, b):
#     return (a + b) + 4
# print(new(23,32))


# def new2(a, b):
#     if a > b:
#         return b
#     elif b < a:
#         return a
# d = new2(8, 4)
# print(d)

def  list_appender(list1, list2, *args):
    my_list = []
    my_list.append(list1)
    my_list.append(list2)
    print(args)
    if args:
        print("This is an argument", args)
        my_list.append(args)
    print("This is whole list", my_list)


l1 = [1, 3, 4, 3, 3]
l2 = [2, 3, 5, 7, 5]
l3 = ["world", "age", "salary"]
l4 = [2, 3]
l5 = []

list_appender(l1, l2)

# def list_appender(list1,**kwargs):
#     my_list = []
#     my_list.append(list1)
#     if kwargs:
#         print("This is an argument", kwargs["name"])
#         my_list.append(kwargs["name"])
#         my_list.append(kwargs["age"])
#     print("This is a whole list")
# l1 = [1, 3, 4, 4]
# l2 = [2, 4, 3, 3, 3]
#
# list_appender(l1, name = "Mario", age = "21")
