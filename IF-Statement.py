print('Hello World!');

Cars = ['audi', 'bmw', 'subaru', 'toyota','nissan'];
print(Cars);
print('\n');

#Use of if Statement
Car = Cars[0];
if Car == 'audi':
    print(Car.upper());
print('\n');

#Use of if With For(Cheking Equality)
for Car in Cars:
    if Car == 'bmw':
        print(Car.upper());
    else:
        print(Car.title());
print('\n');

#Use of if With For(Cheking In-equality)
for Car in Cars:
    if Car != 'bmw':
        print(Car.upper());
    else:
        print(Car.title());
print('\n');

#Use of if With For(Cheking Equality/In-equality using numeric list)
Ages = [12,13,14,15,16,17,18,20,25,30];
print(Ages);
print('\n');
for Age in Ages:
    if Age == 20:
        print('True');
    else:
        print('False');
print('\n');

for Age in Ages:
    if Age == 20:
        print('True');
    else:
        print('False');
print('\n');

#Use of multiple if-else statements(elif)
Percentage = 40;
if Percentage >= 80:
    print('A+');
elif Percentage >= 70:
    print('A');
elif Percentage >= 60:
    print('B');
elif Percentage >= 50:
    print('C');
elif Percentage >= 45:
    print('D');
else:
    print('You failed');

#That's All
#Thank You