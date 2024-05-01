main_value = input()

A, B, C = main_value.split()
A = int(A)
B = int(B)
C = int(C)

lists = [A, B, C]
lists.sort()

for i in lists:
    print(i)

print("\n{}\n{}\n{}".format(A, B, C))