main_value = input()

X, Y = main_value.split()

X = float(X)
Y = float(Y)

if X > 0 and Y > 0:
    print("Q1")
elif X > 0 > Y:
    print("Q4")
elif X < 0 < Y:
    print("Q2")
elif X < 0 and Y < 0:
    print("Q3")
elif X == 0 and Y == 0:
    print("Origem")
elif X == 0:
    print("Eixo Y")
elif Y == 0:
    print("Eixo X")