def show_musicians(names):
    for name in names:
        print(name.title())
musicians = ['eric','polly','randi']
show_musicians(musicians)
def make_great(names):
    name = []
    while names:
        popped = names.pop()
        new = 'The great'+ ' ' + popped
        name.append(new)
    return name
musicians_1 = make_great(musicians)
show_musicians(musicians_1)

from make_car import *
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

#import module_name
#from module_name import function_name
#from module_name import function_name as fn
#import module_name as mn
#from module_name import *