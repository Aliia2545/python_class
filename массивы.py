# a = [('Tom', 'Sam', 'Bob'), (25, 26, 29), ('01111222', '011113333', '011114444'), (67, 74, 82), (80.6, 78.5, 82.6)]
#
# b = ('dog', 'cat', 34)
# a = 0
# for i in range(len(b)):
#     # print(b[i])
#     print(i)
#     # print(b)

# num = 0
# while num < len(b):
#     print(b[num])
#     num += 1



# list_1=['Tom', 23, 65.7, True, a, (a,)]
# print(type(list_1[-1]), type(list_1[-2]))

# name_1 = ['Tom', 'Sam', 'Bob', 'Kate', 'Alice']
# name_2 = ' '.join(name_1)
# print(name_2)

# list_2 = ('name', 'surname', 'age', 'phone_number', 'address', 'email', 'job', 'gender', 'education', 'family', 'children', 'old_job', 'background', 'hobby', 'salary')
# list_22 = list_2[0:3]
# list_23 = list_2[3:6]
# list_24 = list_2[6:9]
# list_25 = list_2[9:12]
# list_26 = list_2[12:15]
#
# print(list_22, list_23, list_24, list_25, list_26)
# print(len(list_2))


# NAMES = ['JACK', 'JIMMY', 'JACKSON', 'JHON', 'JACKSON', 'JHON',  'JIMMY', 'JACKSON', 'JHON','JACK', 'JIMMY', 'JACK', 'JACKSON', 'JHON', 'JACKSON', 'JHON','JACK', 'JIMMY', 'JACK', 'JACKSON', 'JHON',]
# print(NAMES.count('JACK'))

# NAMES = ['JACK', 'JIMMY', 'JACKSON', 'JHON', 'JACKSON', 'JHON',  'JIMMY', 'JACKSON', 'JHON','JACK', 'JIMMY', 'JACK', 'JACKSON', 'JHON', 'JACKSON', 'JHON','JACK', 'JIMMY', 'JACK', 'JACKSON', 'JHON',]
# print(len(NAMES))
# name_1 = NAMES[1:10:2] + NAMES[10:]
# print(name_1)
# print(len(name_1))


a = []
b = []
a.append(["Aliia", 1998, "python"])
b.extend(["Aliia", 1998, "python"])
# a.append(1998)
# a.append("python")
# a.extend("python")

print(len(a))
print(len(b))
