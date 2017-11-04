sandwich_orders = ['bacon','cheese','club','deli']
finished_sandwiches = []
if sandwich_orders:
    for sandwich_order in sandwich_orders:
        print('I made your',sandwich_order,'sandwich')
        finished_sandwiches.append(sandwich_order)
print('Sandwiches made: ',finished_sandwiches)

sandwich_orders = ['bacon','pastrami','cheese','pastrami'
                    ,'club','pastrami']
finished_sandwiches =[]
print('The deli has run out of pastrami.')
count = 0
while 'pastrami' in sandwich_orders:
    if sandwich_orders[count] == 'pastrami':
        del(sandwich_orders[count])
    else:
        finished_sandwiches.append(sandwich_orders[count])
        count += 1
print('Sandwiches made: ',finished_sandwiches)

print('------poll------')
response_dict = {}
flag = True
while flag:
    poll = input('Do you want to continue to poll(quit to exit)? ')
    if poll == 'quit':
        flag = False
        break
    else:
        name = input('Enter your name: ')
        place = input('If you could visit one place in the world,'
                      'where would you go? ')
        response_dict[name] = place
print(response_dict)
for key,val in response_dict.items():
    print(key.title(),'wants to visit',val.title())
