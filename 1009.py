sellers_name = input()
fixed_salary = float(input())
sales_total = float(input())

consider = sales_total * (15/100)

final_salary = fixed_salary + consider

print('TOTAL = R$ {:.2f}'.format(final_salary))
