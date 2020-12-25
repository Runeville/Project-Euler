divider = 1

for i in range(10, 10000000000, 10):
    for x in range(2, 21):
        if i % x != 0:
            break
    else:
        divider = i
        break

print(divider)
