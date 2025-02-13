# import random

# num = random.randint(1, 21)

# print('Guess a number between 1 to 20:')
# guessed_num = int(input())

# if guessed_num > num:
#     print('Guess a smaller number')
# elif guessed_num < num:
#     print('Guess a greater number')
# else:
#     print('Correct guess')


import random

# Generate a random number between 1 and 20
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Allow the player to guess up to 6 times
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break  # This condition is the correct guess!

# Check if the player guessed correctly
if guess == secretNumber:
    print(f'Good job! You guessed my number in {guessesTaken} guesses!')
else:
    print(f'Nope. The number I was thinking of was {secretNumber}.')
