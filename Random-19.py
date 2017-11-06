class resturant():
    def __init__(self,resturant_name,cuisine_type):
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_resturant(self):
        print(self.resturant_name.title())
        print(self.cuisine_type.title())
    def open_resturant(self):
        print('The retsurant is open.')
    def set_number_served(self,number_served):
        self.number_served = number_served
        print(number_served)
    def increament_number_served(self,increament):
        self.number_served += increament

resturant_1 = resturant('Noman','dhaba')
resturant_1.describe_resturant()
resturant_1.open_resturant()
resturant_1.set_number_served(9)
resturant_1.increament_number_served(2)
print(resturant_1.number_served)