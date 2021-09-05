# problem 2
# a = 'php'
# language= ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in language:
#     # print(i)
#     if i == 'php':
#         break
#     print(i)
#problem4
language= ['go', 'java', 'php', 'python', 'javascript', 'ruby', 'pator', 'dart']
# print(len(language))
# for i in range(0, len(language), 2):
    # print(i+1, language[i])


# for i in range(len(language)-1, -1, -1):
#     print(i+1 , language[i])

i = len(language) - 1
while i >= 0:
    print(i + 1, language[i])
    i -= 1

# # a = int(input())
# result = a
# for _ in range(5):
#     # result *= a
#     print(result)
# a = input()
# for i in a:
#     if "j" == i:
#         print(a)
#         break
# print("It is no J in your name")
#
# print(len(a))