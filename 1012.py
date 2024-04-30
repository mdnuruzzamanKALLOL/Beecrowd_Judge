main_value = input()

A, B, C = main_value.split()

A = float(A)
B = float(B)
C = float(C)

pi = 3.14159

TRIANGULO = (A * C)/2
CIRCULO = C**2 * pi
TRAPEZIO = ((A+B)/2) * C
QUADRADO = B**2
RETANGULO = A * B

print("TRIANGULO: {:.3f}".format(TRIANGULO))
print("CIRCULO: {:.3f}".format(CIRCULO))
print("TRAPEZIO: {:.3f}".format(TRAPEZIO))
print("QUADRADO: {:.3f}".format(QUADRADO))
print("RETANGULO: {:.3f}".format(RETANGULO))
