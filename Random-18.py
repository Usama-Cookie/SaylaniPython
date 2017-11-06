class resturant():
    def __init__(self,resturant_name,cuisine_type):
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type
    def describe_resturant(self):
        print(self.resturant_name.title())
        print(self.cuisine_type.title())
    def open_resturant(self):
        print('The retsurant is open.')
resturant_1 = resturant('Noman','dhaba')
resturant_1.describe_resturant()
resturant_1.open_resturant()

class user():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print('First name:',self.first_name.title())
        print('Last name:',self.last_name.title())
        full_name = self.first_name + ' ' + self.last_name
        self.fullname = full_name
    def greet_user(self):
        print('Hello!',self.fullname.title())
user_1 = user('muhammad usama','khan')
user_1.describe_user()
user_1.greet_user()