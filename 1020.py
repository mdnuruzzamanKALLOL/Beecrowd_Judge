total_day = int(input())

years = total_day // 365
var1 = total_day % 365
months = var1 // 30
day = var1 % 30

print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(years, months, day))
