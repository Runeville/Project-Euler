number = 1000
Simple_numbers = []
j = []
a = 0
for i in range(2, 10000000000000):
    if len(Simple_numbers) < number:
        a = i
        while a != 0:
            if i % a == 0:
                j.append(a)
                if len(j) > 2:
                    j = []
                    break
            a -= 1
        else:
            j = []
            Simple_numbers.append(i)
    else:
        break
print(Simple_numbers[-1])
