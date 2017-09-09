''' Question 11:
A website requires the users to input username and password to
register. Write a program to check the validity of password input by
users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords
and will check them according to the above criteria. Passwords that
match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
Hints:
In case of input data being supplied to the question, it should be
assumed to be a console input. '''

import re
va = []
lis = []
n = 0
x = 0
username = input('Enter User name: ')
password = input('Enter passwords: ')
l = len(password)
while n < l:
    for string in password:
        if string == ',':
            lis.append(password[x:n])
            x = n
            x += 1
        n += 1
lis.append(password[x:n])

for li in lis:
    if len(li) >= 6 and len(li) <=12:
        if not re.search("[a-z]",li):
            continue
        elif not re.search("[0-9]",li):
            continue
        elif not re.search("[A-Z]",li):
            continue
        elif not re.search("[$#@]",li):
            continue
        elif re.search("\s",li):
            continue
        else:
            pass
        va.append(li)
    else:
        pass
print(lis)
print(va)