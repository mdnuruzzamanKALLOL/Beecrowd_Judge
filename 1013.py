main_value = input()
a, b, c = main_value.split()
a = int(a)
b = int(b)
c = int(c)

if a>b and a>c:
    print(a,"eh o maior")
elif b>c:
    print(b, "eh o maior")
else:
    print(c, "eh o maior")
