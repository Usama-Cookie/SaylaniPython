from random import randint

null = 3
optn = ['y','n']
ans = input('Do you want to play the game? y/n: ')
while ans == optn[0]:
    numb = randint(1, 10);
    while null > 0:
        num = int(input('Guess a number in range 1-10: '))
        print(num)
        if num == numb:
            print('You Win...')
            break
        else:
            null -= 1
            if null > 1:
                print('You Lose...', 'You have', null, 'chance(s) left.')
            elif null == 1:
                print('You Lose...', 'This is your last chance.')
            else:
                print('You Lose...')
    ans = input('Do you want to play again? y/n: ')
    null = 3