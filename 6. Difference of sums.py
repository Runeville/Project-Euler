dif = 0
sum1 = 1
sum2 = 1

for i in range(2, 101):
    sum1 += i**2

for i in range(2, 101):
    sum2 += i
else:
    sum2 **= 2

dif = sum2 - sum1
print(dif)
