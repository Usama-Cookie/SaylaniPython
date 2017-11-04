favourite_pizza = ['Margherita','Funghi','Capricciosa']
for pizza in favourite_pizza:
    print(pizza,'pizza contains: Tomato sauce, Mozzarella.')
print("I don't like pizza, I didn't even knew the names, "
      "I just googled these names and wrote here....")
animals = ['fox','jackal','wolf']
for animal in animals:
    print(animal.title(),'is a carnivore.')
print('The can attack you, kill you and eat you...')

foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
print('The first three items in the list are:',foods[:3])
print('Three items from the middle of the list are:',foods[1:4])
print('The last three items are:',foods[-3:])

favourite_pizza = ['Margherita','Funghi','Capricciosa','Quattro Stagioni']
friends_pizza = ['Margherita','Funghi','Capricciosa','Neapolitan']
print('My favourite pizzas are:')
pizza = [pizza for pizza in favourite_pizza]
print(pizza)
print('My friends favourite pizaas are:')
pizza = [pizza for pizza in friends_pizza]
print(pizza)
