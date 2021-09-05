'''from random import random
a = int(random() * 100)
b = int(random() * 100)
c = a % 2
d = b % 2
print(a, b, c, d)
if a % 2 and b % 2 or a % 2 == 0 and b % 2 == 0:
    a += 1
    print(a, b)
if a % 2:
    print(a)
else:
    print(b)'''
'''
number = int(input("input your number:"))
transfer = int(input("choose the transfer (to bytes: 1, to kilobytes: 2):"))
if transfer == 1:
    result = number * 1024
    print("your result is : ", round(result, 2), "bytes")
elif transfer == 2:
    result = number / 1024
    print("your result: ", round(result, 2), "kilobytes")
else:
    result = 0
    print("enter the correct transfer!")
'''
'''
a = int(input("enter the year"))
if a % 4 != 0:
    print("usual year")
elif a / 100 and a / 400:
    print("leap year")
else:
    print("usual year")
'''
'''
x = 4
y = -6
if x >= 0 and y >= 0:
    print("1")
elif x >= 0 and y < 0:
    print("2")
elif x < 0 and y < 0:
    print("3")
elif x < 0 and y >=0:
    print("4")
'''
'''
x = 0
if x > 0:
    y = 2 * x - 10
    print(y)
elif x == 0:
    y = 0
    print(y)
elif x > 0:
    y = 2 * abs(x) - 1
    print(y)
'''


