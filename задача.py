a = int(input("enter a"))
b = int(input("enter b"))
c = int(input("enter c"))
if a > b and a > c:
    print("max", a)
elif b > a and b > c:
    print("max", b)
elif c > a and c > b:
    print("max", c)
if a < c and a < b:
    print("min", a)
elif b < a and b < c:
    print("min", b)
elif c < a and c < b:
    print("min", c)
