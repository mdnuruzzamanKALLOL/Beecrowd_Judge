N = float(input())

hundred = int(N // 100)
var1 = N % 100
fifty = int(var1 // 50)
var2 = var1 % 50
twenty = int(var2 // 20)
var3 = var2 % 20
ten = int(var3 // 10)
var4 = var3 % 10
five = int(var4 // 5)
var5 = var4 % 5
two = int(var5 // 2)
one = int(var5 % 2)

var6 = float(var5 % 1)*100
coin_fifty = int(var6 // 50)
var7 = (var6 % 50)
coin_twenty_five = int(var7 // 25)
var8 = (var7 % 25)
coin_ten = int(var8 // 10)
var9 = (var8 % 10)
coin_five = int(var9 // 5)
coin_one = int(var9 % 5)

print("NOTAS:\n{} nota(s) de R$ 100.00\n{} nota(s) de R$ 50.00\n{} nota(s) de R$ 20.00\n{} nota(s) de R$ 10.00\n{} nota(s) de R$ 5.00\n{} nota(s) de R$ 2.00\nMOEDAS:\n{} moeda(s) de R$ 1.00\n{} moeda(s) de R$ 0.50\n{} moeda(s) de R$ 0.25\n{} moeda(s) de R$ 0.10\n{} moeda(s) de R$ 0.05\n{} moeda(s) de R$ 0.01".format(hundred, fifty, twenty, ten, five,two, one, coin_fifty, coin_twenty_five, coin_ten, coin_five, coin_one))