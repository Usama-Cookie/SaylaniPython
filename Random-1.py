names = ['kamran','kashif','imran','tayyab','ibrar']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print('Hello! ' + names[0].title())
print('Hello! ' + names[1].title())
print('Hello! ' + names[2].title())
print('Hello! ' + names[3].title())
print('Hello! ' + names[4].title())
bikes = ['Honda','Suzuki','Yamaha','Unique','Super Power']
message_1 = bikes[0] + ' is the leading bike brand, ' + bikes[1] + \
            ' bikes are way too expensive, ' + bikes[2] + ' bikes have ' \
            'good looks, ' + bikes[3] + ' is the last bike I had. ' + \
            'Now, everyone is forcing me to buy ' + bikes[4] + '.'
print(message_1)
guests = ['Kamran','Kashif','Imran']
print(guests[0] + ' join me at dinner today.')
print(guests[1] + ' join me at dinner today.')
print(guests[2] + ' join me at dinner today.')
print(guests[0] + ' & ' + guests[1] + ' Are joining, ' + guests[2] + " can't come.")
del guests[2]
guests.append('Tayyab')
print(guests[0] + ' join me at dinner today.')
print(guests[1] + ' join me at dinner today.')
print(guests[2] + ' join me at dinner today.')
print('Hey guys! I found a bigger dinner table. '
      'Lets add more friends to the dinner...')
guests.insert(0,'Ibrar')
guests.insert(2,'Salman')
guests.append('Imran')
print(guests[0] + ' join me at dinner today.')
print(guests[1] + ' join me at dinner today.')
print(guests[2] + ' join me at dinner today.')
print(guests[3] + ' join me at dinner today.')
print(guests[4] + ' join me at dinner today.')
print(guests[5] + ' join me at dinner today.')
print('I am inviting:',len(guests),'people.')
print('I can invite only two pepole for dinner...')
popped = guests.pop()
print('Sorry ' + popped + "! I can't invite you on dinner")
popped = guests.pop()
print('Sorry ' + popped + "! I can't invite you on dinner")
popped = guests.pop()
print('Sorry ' + popped + "! I can't invite you on dinner")
popped = guests.pop()
print('Sorry ' + popped + "! I can't invite you on dinner")
print(guests[0],'&',guests[1],'You are invited on the dinner.')
del guests[0]
del guests[0]
print(guests)
