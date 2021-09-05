# problem 5
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(1, 10):
#     print(i)
#     j in range(9, 0, -1):
#     print(j)

# a = list(range(1, 10))
# b = list(range(10, 0, -1))
# d = a + b
# # for i in d:
# #     print(i)
# i = 0
# while i < len(d):
#     print(d[i])
#     i += 1
# print(len(d))


# a = 1
# while a < 10:
#     print(a)
#     a += 1
# b = -10
# while b < 0:
#     print(b)
#     b -= -1

# problem 6
# names = ('Maksat', 'Aibek', 'Daniyar', 'Atai', 'Salavat', 'Begaiym')
# for name in range(0, (len(names)), 2):
#     print(names[name])
# i = 0
# while i < len(names):
#     print(names[i])
#     i += 2


# problem 7
names = (
'Maksat', 'Aibek', 'Daniyar', 'Atai', 'Salavat', 'Adinai', 'Joomart', 'Alymbek', 'Ermek', 'Dastfan', "Bekmamat",
'Aslan')
# for name in range(0, (len(names)), 2):
#     print(names[name])
# i = 0
# while i < len(names):
#     print(names[i])
#     i += 2

# problem 8
# a = 222
# # if 99 < a <= 999:
# if len(str(a)) == 3:
#     print("da, trex znachnaya")
# if a > 0 and a % 2 == 0:
#     print(" polojitelnaya i chetnaya")
# if a % 31 == 0:
#     print("delitsya na 31")
# if (a > 100 and a % 17 == 0) or (a > 150 and a == 13**2):
#     print(a)
# else:
   # print("wrong")

# problem 9

a = 0
b = 0
for i in range(-100, 101):
    if i % 13 == 0 and i % 2 == 0:
        num = i ** 2
        a += 1
        print(i, num)

        if i % 2 != 0:
            b += 1
            print(i)
print(a, b)

# for i in range(-100, 101, 7):
#     if i % 2 != 0:
#         a += 1
#         print(i)
# print(a)


# i = -100
# while i < 100:
#     if i % 13 == 0 and i % 2 == 0:
#         i **= 2
#         print(i)
#         i += 1
