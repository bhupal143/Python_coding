
guessnumimport random
secretnumber = random.randint(1, 20)
#Ask user to enter the number
for guessno in range(1, 7):
    print('Please enter a number between 1 and 20')
    guessnum = input()
    if int(guessnum) > secretnumber:
        print('Your guess is too high')
    elif int(guessnum) < secretnumber:
        print('Your guess is too low')
    else:
        break
if  secretnumber == int(guessnum):
    print('Your guessed number  ' +guessnum +' is correct. You have guessed the correct number in ' +str(guessno) +' attempts.')
else:
    print('Betterluck next time. The correct number is ' +str(secretnumber) +'.')





