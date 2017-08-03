#CONTINUING FROM LAST PROGRAM

Bikes = ['Yamaha','Suzuki','Honda','Unique','Super Power'];
print(Bikes);

#FOR LOOP
for Bike in Bikes:
    print(Bike);
print('\n');
print(Bikes,'\n');

#USE OF RANGE FUNCTION WITH FOR LOOP
for a in range(1,10):
    print(a);
print('\n');

for b in range(0,20,2):
    print(b);
print('\n');

#GENERATING A LIST OF NUMBER USING LIST FUNCTION
Numbers = list(range(0,100,10));
print(Numbers);
print('\n');

#GENERATING A LIST OF NUMBERS USING FOR LOOP
Numbers = [];
for c in range(0,100,10):
    Numbers.append(c);
print(Numbers);
print('\n');

#GENERATING A LIST IN A DIFFERENT WAY
Numbers = [a for a in range(0,100,10)];
print(Numbers,'\n');

#USING LIST FOR FINDING THE MAXIMUM, MINIMUM NUMBER & SUM OF WHOLE LIST
a = min(Numbers);
b = max(Numbers);
c = sum(Numbers);
print('Smallest number is:',a,'\n');
print('Largest number is:',b,'\n');
print('Sum of the List is:',c,'\n');

#THANK YOU
#THATS ALL FROM 29 JULY CLASS