car = input('What kind of rental car you want? ')
print('Let me see if I can find you a',car + '.')

people = int(input('How many people are there in you dinner group? '))
if people <= 8:
    print('Your table is ready.')
else:
    print("You'll have to wait for a table.")

number = int(input('Enter any nunber: '))
if number > 0:
    num = number % 10
    if num == 0:
        print(number,'is a multiple of 10')
    else:
        print(number, 'is a not a multiple of 10')
else:
    print('Error! You entered 0....')
