mySum = 0
i = 1
a = i

while i <= 4000000:
    i = i + a
    a = i - a
    if i % 2 == 0:
        mySum = mySum + i

print(mySum)
