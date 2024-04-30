import math

main_value = input()

A, B, C = main_value.split()

A = float(A)
B = float(B)
C = float(C)

m_cal = B**2 -4*A*C

if A == 0 or m_cal < 0:
    print("Impossivel calcular")
else:
    R1 = (-B + math.sqrt(m_cal)) / (2*A)
    R2 = (-B - math.sqrt(m_cal)) / (2*A)

    print("R1 = {:.5f}\nR2 = {:.5f}".format(R1, R2))
