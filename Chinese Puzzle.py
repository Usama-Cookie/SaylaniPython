''' Question 1:
Write a program to solve a classic ancient Chinese puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a
farm. How many rabbits and how many chickens do we have?
Hint:
Use for loop to iterate all possible solutions. '''

i = 0
heads = int(input('Enter the number of heads: '))
legs = int(input('Enter the number of legs: '))
for chickens in range(heads + 1):
    rabbits = heads - chickens
    i += 1
    if 2 * chickens + 4 * rabbits == legs:
        print('There are chickens: ',chickens,'\n','There are Rabbits: ',rabbits)
        break
    elif 2 * chickens + 4 * rabbits != legs and i == heads + 1:
        print('Impossible')
