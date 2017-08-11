print('Hello World');

#Slicing a List
Bikes = ['Yamaha','Suzuki','Honda','Unique','Super Power','Bionic'];
print(Bikes,'\n');

Bike = Bikes[0:3];
print(Bike,'\n');

Bike = Bikes[:3];
print(Bike,'\n');

Bike = Bikes[2:];
print(Bike,'\n');

Bike = Bikes[2:5];
print(Bike,'\n');

#Printing The Whole List in Reverse Order
Bike = Bikes[:0:-1];
print(Bike,'\n');

print(Bikes,'\n');

#Using FOR Loop
for Bike in Bikes[:4]:
    print(Bike.upper());

print('\n');

#TUPLES
tupple = (10,5);
print(tupple[0]);
print(tupple[1]);
print('\n');

'''To Change a Value in This Type of List
    need to re-write the tuple again'''
tupple = (11,15);
print(tupple[0]);
print(tupple[1]);
