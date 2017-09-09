''' Question 10:
Write a program to compute:
f(n)=f(n-1)+100 when n>0
and f(0)=1
with a given n input by console (n>0).
Example:
If the following n is given as input to the program:
5
Then, the output of the program should be:
500
In case of input data being supplied to the question, it should be
assumed to be a console input.
Hints:
We can define recursive function in Python. '''

a = 1
def rec(num):
    return a + 100
num = int(input('Input a number(must be > 0 ): '))
if num != 0:
    for n in range(num):
        n += 1
        a = rec(n)
else:
    a
print(a)
