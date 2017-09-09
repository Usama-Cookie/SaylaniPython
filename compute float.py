''' Question 9:
Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n
input by console (n>0).
Example:
If the following n is given as input to the program:
5
Then, the output of the program should be:
3.55
In case of input data being supplied to the question, it should be
assumed to be a console input.
Hints:
Use float() to convert an integer to a float '''


num = int(input('Input a number(must be greater zero): '))
n = 1
x2 = 0.0
while n <= num:
    x = float(n/(n+1))
    x2 = x2 + x
    n += 1
print(round(x2,2))