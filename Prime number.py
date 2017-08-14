num = int(input('Enter any number: '))
print('You entered: ',num)
numb = 1
factors =[]
while numb != num+1:
    if num % numb == 0:
        factors.append(numb)
        numb += 1
    else:
        numb += 1

print(factors)
if len(factors) == 2:
    print(num,'is a prime number.')
else:
    print(num, 'is a not prime number.')