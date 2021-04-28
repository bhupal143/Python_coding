import random, sys
#These varibles keep track of wins, loss and ties
while True:
    wins = 0
    ties = 0
    losses = 0
    print('Game Name: Rock, paper, Scissors')
    print('Please start the  Game')
    print('You have 10 attempts to play the game')
    print('Status: %s wins, %s losses, %s Ties' %(wins, losses, ties))
    while True:
        count = 0
        while count <= 10:
            print('Please enter your move: (r)ock (p)aper (s)cissorso or (q)uit')
            print('Note:Type only one among p, r, s or q')
            playermove = input()
            if playermove == 'q':
                sys.exit()
            elif playermove == 'p' or playermove == 'r' or playermove == 's':
                break
            else:
                print('Invalid Move')
        #display what player choose
        if playermove == 'r':
            print('Rock versus.....')
        elif playermove == 'p':
            print('Paper versus.....')
        elif playermove == 's':
            print('scissors versus.....')
        #display what computer choose
        randomnumber = random.randint(1,3)
        if randomnumber == 1:
            computermove = 'r'
            print('Rock')
        elif randomnumber == 2:
            computermove = 'p'
            print('paper')
        elif randomnumber == 3:
            computermove = 's'
            print('Scissors')
        #Display and record the Wins/losses/ties
        #r>s, p>r, s>p.
        if playermove == computermove:
            print('It is tie')
            ties = ties+1
        elif playermove == 'r' and computermove == 's':
            print('You win!')
            wins = wins+1
        elif playermove == 'p' and computermove == 'r':
            print('You win!')
            wins = wins+1
        elif playermove == 's' and computermove == 'p':
            print('You win!')
            wins = wins+1
        elif playermove == 's' and computermove == 'r':
            print('You Lose')
            losses = losses+1
        elif playermove == 'r' and computermove == 'p':
            print('You Lose')
            losses = losses+1
        elif playermove == 'p' and computermove == 's':
            print('You Lose')
            losses = losses+1
        count = count+wins+losses+ties
        if count == 10:
            break
    print('Thanks for playing the game')
    print('Your chances completed')
    print('Ending Status: %s wins, %s losses, %s Ties' %(wins, losses, ties))



