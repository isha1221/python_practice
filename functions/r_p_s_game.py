import random
import sys

print('Rock, Paper, Scissors')

win = 0
loss = 0
tie = 0

while True:
    while True:
        print('Enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit:')
        move = input().lower()

        if move == 'q':
            print(f"Final Scores: Wins: {win}, Losses: {loss}, Ties: {tie}")
            sys.exit()

        if move in ['r', 'p', 's']:
            break
        print('Invalid input. Please enter "r", "p", "s", or "q".')

    # Player's move
    if move == 'r':
        print('Rock versus...')
    elif move == 'p':
        print('Paper versus...')
    else:
        print('Scissors versus...')

    # Computer's move
    rand_num = random.randint(1, 3)
    if rand_num == 1:
        comp_move = 'r'
        print('Rock')
    elif rand_num == 2:
        comp_move = 'p'
        print('Paper')
    else:
        comp_move = 's'
        print('Scissors')

    # Game conditions
    if move == comp_move:
        print("It's a tie!")
        tie += 1
    elif (move == 'r' and comp_move == 's') or (move == 's' and comp_move == 'p') or (move == 'p' and comp_move == 'r'):
        print("You win!")
        win += 1
    else:
        print("You lose!")
        loss += 1

    # Display scores
    print(f"Score: Wins: {win}, Losses: {loss}, Ties: {tie}")
