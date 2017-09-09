''' Question 4:
Please write a program which count and print the numbers of each
character in a string input by console.
Example:
If the following string is given as input to the program:
abcdefgabc
Then, the output of the program should be:
a,2
c,2
b,2
e,1
d,1
g,1
f,1
Hints:
Use dict to store key/value pairs.
Use dict.get() method to lookup a key with default value. '''


word_count = {}
string = str(input('Input string: '))
for string in string:
    word_count[string] = word_count.get(string,0)+1
#print(word_count)
for key,value in word_count.items():
    print(key,',',value)