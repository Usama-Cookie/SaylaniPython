people = [{'first_name':'logan','last_name':'wolverine','age':300,
           'city':'Karachi'},
          {'first_name':'eric','last_name':'magneto','age':500,
           'city':'Lahore'},
          {'first_name': 'imarn', 'last_name': 'khan', 'age': 70,
           'city': 'Peshawar'}
          ]
if people:
    for person in people:
        for key,val in person.items():
            print(key.title(),':',str(val).title())

suzie = {'kind':'cat','owner':'logan'}
mate = {'kind':'dog','owner':'eric'}
loki = {'kind':'rabbit','owner':'imran'}
pets = [suzie,mate,loki]
if pets:
    for pet in pets:
        for key, val in pet.items():
            print(key.title(), ':', str(val).title())

favorite_number = {'eric':[5,10,15],'clark':[9,18,27],
                   'john':[13,26,39],'admin':[69,96],'polly':[45]}
for nam,num in favorite_number.items():
    if len(num)>1:
        print(nam.title()+ "'s favorite numbers are:",str(num))
    else:
        print(nam.title()+ "'s favorite number is:",str(num))

cities = {
          'karachi':{'country':'pakistan','population':'30 million',
                     'fact':'Largest city and former capital of Pakistan'},
          'delhi':{'country':'india','population':'25 million',
                   'fact':'The national capital of India'},
          'dhaka':{'country':'bangladesh','population':'20 million',
                   'fact':'It is the industrial, commercial, and '
                          'administrative center of Bangladesh'}
          }
for city,info in cities.items():
    print(city.title())
    for key,val in info.items():
        print(key.title(),':',val.title())
