N = int(input())

hours = N // 3600
var1 = N % 3600
minutes = var1 // 60
seconds = var1 % 60

print("{}:{}:{}".format(hours, minutes, seconds))
