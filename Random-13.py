flag = True
while flag:
    topping = input('Enter pizza topping(quit to confirm): ')
    if topping == 'quit':
        flag = False
        break
    else:
        print('Adding', topping + '.')

flag = True
while flag:
    age = input('Enter your age to know the ticket price'
                '(quit to confirm): ')
    if age == 'quit':
        flag = False
        break
    else:
        if int(age) < 3:
            print('The ticket is free.')
        elif int(age) >= 3 and int(age) <= 12:
            print('The ticket charges are $10.')
        elif int(age) > 12:
            print('The ticket charges are $15.')

count = 0
while count < 10:
    age = input('Enter your age to know the ticket price')
    count += 1
    if int(age) < 3:
        print('The ticket is free.')
        print('You have',10-count,'entries left.')
    elif int(age) >= 3 and int(age) <= 12:
        print('The ticket charges are $10.')
        print('You have',10-count,'entries left.')
    elif int(age) > 12:
        print('The ticket charges are $15.')
        print('You have',10-count,'entries left.')