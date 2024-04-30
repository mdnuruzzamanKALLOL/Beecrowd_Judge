amount = int(input())

hundred = amount // 100
var1 = amount % 100
fifty = var1 // 50
var2 = var1 % 50
twenty = var2 // 20
var3 = var2 % 20
ten = var3 // 10
var4 = var3 % 10
five = var4 // 5
var5 = var4 % 5
two = var5 // 2
one = var5 % 2

print("{}\n{} nota(s) de R$ 100,00\n{} nota(s) de R$ 50,00\n{} nota(s) de R$ 20,00\n{} nota(s) de R$ 10,00\n{} nota(s) de R$ 5,00\n{} nota(s) de R$ 2,00\n{} nota(s) de R$ 1,00".format(amount, hundred, fifty, twenty, ten, five, two, one))
