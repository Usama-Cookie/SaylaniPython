''' Question 7:
Assuming that we have some email addresses in the
"username@companyname.com" format, please write program to print the
user name of a given email address. Both user names and company
names are composed of letters only.
Example:
If the following email address is given as input to the program:
john@google.com
Then, the output of the program should be:
john
In case of input data being supplied to the question, it should be
assumed to be a console input.
Hints:
Use \w to match letters. '''

import re
string = input("Enter email address(Both user names and company names are composed of letters only): ")
username = re.match("(\w+)@(\w+).(com)",string)
print(username.group(1))