def display_message():
    print('I am learning about making functions in this chapter...')
display_message()

def favorite_book(title):
    print('One of my favorite books is',title + '.')
favorite_book('Alice in Wonderland')

def make_shirt(size,text):
    print('The size of your shirt is',size,'with',text,'printed on it.')
make_shirt('small','baby')
make_shirt(text='keep calm',size='medium')

def make_shirt(size='large',text='I love Python'):
    print('The size of your shirt is',size,'with',text,'printed on it.')
make_shirt()
make_shirt(size='medium')
make_shirt(size='small',text='anything')

def describe_city(city,country):
    print(city.title(),'is in',country.title())
describe_city('karachi','pakistan')
describe_city('dhaka','bangladesh')
describe_city('newyork','america')