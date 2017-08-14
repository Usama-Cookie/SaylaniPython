from random import randint
num = int(input('Enter the max. range of number you want to generate: '))
nill = 0
random = []
while nill != num:
    numb = randint(1, num)
    if numb not in random:
        random.append(numb)
        nill += 1

print('Your random number list: ',random)
print('Length of the list is: ',len(random))