def check_for_palindrome(a):
    a = str(a)
    numbers = list(a)
    numbers.reverse()

    if numbers == list(a):
        return int(a)


palindrome = 0

for x in range(100, 1000):
    for y in range(100, 1000):
        number = check_for_palindrome(x * y)
        if number is not None and number > palindrome:
            palindrome = number

print(palindrome)
