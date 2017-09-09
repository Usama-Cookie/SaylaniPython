''' Question 13:
Define a class with a generator which can iterate the numbers, which
are divisible by 7, between a given range 0 and n.
Hints:
Consider use yield '''


def seven(n):
    for n in range(n+1):
        if n == 0:
            pass
        else:
            if n % 7 == 0:
                yield n
num = int(input('A number: '))
a = seven(num)
for n in seven(num):
    print(n)