import math

main_value_1 = input()
main_value_2 = input()

x1, y1 = main_value_1.split()
x2, y2 = main_value_2.split()

x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

equation = (x2 - x1)**2 + (y2 - y1)**2

Distance = math.sqrt(equation)

print("{:.4f}".format(Distance))


