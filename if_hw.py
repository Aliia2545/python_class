'''a = 17391
b = 546
c = 934
print(a % 17, b % 17, c % 17)
if (a % 17 < b % 17) and (a % 17 < c % 17):
    print("min ostatok(a)", a % 17)
elif (b % 17 < a % 17) and (b % 17 < c % 17):
    print("min ostatok(a)", b % 17)
else:
    print("min ostatok(a)", c % 17)'''
# problem 39
'''x = 13
if x**2 < 172:
    x **= 3
    print("x**3", x)
else:
    print("x**2", x)'''
# problem 5
'''
x = 60001
if x % 2 == 0:
    print("четное число")
else:
    print("нечетное число")
if x % 3 == 0:
    print("делится на 3 без остатка")
else:
    print("остаток от 3:", x % 3)
if x**2 > 1000:
    print("оно больше 1000:", x**2)
else:
    print("оно меньше 1000", x**2)'''
# x = 12
# if x % 2 == 0:
#     if x % 3 == 0:
#         if x**2 > 1000:
#             print("оно больше 1000:  ", x)
#         print("делится на 3 без остатка")
#     else:
#         print("ostatok est")
#     print("четное число")
# else:
#     print("нечетное число:" , x)
# problem 3
# x = 1000
# if x > 0 and x < 100:
#     if 0 <= x < 21 or 57 <= x < 100:
#         print("allow:", x)
#
# else:
#     print("don't allow:", x)
# problem 7
# if True:
#     print("Welcome")
# problem 45
# a = 10 // 5
# b = 10 / 5
# print(a == b)
# if a == b:
#     print(int(a+b))
# probelm 33
# a = int(input("enter a number:"))
# if a < 0:
#     print(f"negative number {a} is this{a}")
# else:
#     print(f"positive number{a}")
# problem 11
# a = -8
# b = 5
# print(a>b, b>a, a==b)
# if a > 0 and b > 0:
#     print("True")
# else:
#     print("False")
a = 10
b = 5
if a > b:
    print("a+2 is " , a + 2)
else:
    print("b + 2" , b + 2)








