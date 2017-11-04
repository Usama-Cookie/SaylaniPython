person = {'first_name':'logan','last_name':'wolverine','age':300,
           'city':'Karachi'}
print(person['first_name'])
print(person['last_name'])
print(str(person['age']))
print(person['city'])
favorite_number = {'eric':5,'clark':9,'john':13,'admin':69,'polly':45}
for nam,num in favorite_number.items():
    print(nam.title()+ "'s favorite number is ",str(num))
glossary = {}
glossary['.title'] = 'makes the string title case'
glossary['.upper'] = 'makes the string upper case'
glossary['.lower'] = 'makes the string lower case'
if glossary:
    for key,val in glossary.items():
        print(key,':',val)
rivers = {'sepik':'new guinea','mississippi':'united states',
          'volga':'russia','zambezi':'africa','nile':'egypt'}
for key,val in rivers.items():
    print('The',key.title(),'runs through',val.title(),'.')
for key in rivers.keys():
    print(key.title())
for val in rivers.values():
    print(val.title())
favorite_languages = {'jen': 'python','sarah': 'c','edward':'java',
                        'phil': 'python'}
poll = ['jen','clark','edward','eric','sarah','phil']
for name in poll:
    if name in favorite_languages.keys():
        print('Thanks for responding,',name.title())
    else:
        print('Please take the poll,',name.title())
        