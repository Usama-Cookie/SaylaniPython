usernames = ['eric','clark','john','admin','polly']
if usernames:
    for username in usernames:
        if username == 'Admin':
            print('Hello',username.title()+', would you '
                                       'like to see a status report?')
        else:
            print('Hello',username.title()+', thank you '
                                       'for logging in again.')
else:
    print('We need to find some users!')

current_usernames = ['eric','clark','john','admin','polly']
new_users = ['sim','elyise','eric','CLARK','mark']
for new_user in new_users:
    if new_user in current_usernames:
        print(new_user,'username not available!')
    else:
        print('Username is available!')

numbers = [num for num in range(1,10)]
for number in numbers:
    if number == 1:
        print(str(number) + 'st')
    elif number == 2:
        print(str(number) + 'nd')
    elif number == 3:
        print(str(number) + 'rd')
    elif number >= 4:
        print(str(number) + 'th')