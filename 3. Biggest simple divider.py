# n = 600851475143
n = 10
i = n
j = 0
k = 0

while i > 0:
    if n % i == 0:
        k = i

        while k > 0:
            if i % k == 0:
                j += 1
            k -= 1
        if j == 2:
            print('The biggest simple divider is', i)
            break
        j = 0
    i -= 1
