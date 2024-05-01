main_value = input()

A, B, C = main_value.split()

A = float(A)
B = float(B)
C = float(C)

if ((A + B) > C) and ((B + C) > A) and ((A + C) > B):
    Perimetr = A + B + C
    print("Perimetro =", Perimetr)
else:
    Area = ((A + B) * C) / 2
    print("Area =", Area)