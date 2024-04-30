main_value = input()

X, Y = main_value.split()
X = int(X)
Y = int(Y)

if X == 1:
    total = 4.00 * Y
    print("Total: R$ {:.2f}".format(total))
elif X == 2:
    total = 4.50 * Y
    print("Total: R$ {:.2f}".format(total))
elif X == 3:
    total = 5.00 * Y
    print("Total: R$ {:.2f}".format(total))
elif X == 4:
    total = 2.00 * Y
    print("Total: R$ {:.2f}".format(total))
elif X == 5:
    total = 1.50 * Y
    print("Total: R$ {:.2f}".format(total))