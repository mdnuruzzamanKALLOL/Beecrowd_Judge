main_value = input()

A, B, C = main_value.split()

A = float(A)
B = float(B)
C = float(C)

lists = [A, B, C]
lists.sort(reverse=True)
A, B, C = lists

if A >= (B + C):
    print("NAO FORMA TRIANGULO")
else:
    if A ** 2 == (B ** 2 + C ** 2):
        print("TRIANGULO RETANGULO")
    if A ** 2 > (B ** 2 + C ** 2):
        print("TRIANGULO OBTUSANGULO")
    if A ** 2 < (B ** 2 + C ** 2):
        print("TRIANGULO ACUTANGULO")
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif A == B or A == C or B == A or B == C or C == A or C == B:
        print("TRIANGULO ISOSCELES")

