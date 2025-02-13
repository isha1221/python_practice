import random

def play_game():
    # Generate a random number
    num = random.randint(1, 100)
    attempts = 10  # Max attempts
    count = 0  # Attempt counter
    
    print("\nGuess a number between 1 and 100:")
    
    while count < attempts:
        try:
            guessed_num = int(input(f"Attempt {count + 1}/{attempts}: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        count += 1
        
        if guessed_num > num:
            print("Guess a smaller number!")
        elif guessed_num < num:
            print("Guess a greater number!")
        else:
            print(f"Bravo! You guessed it in {count} attempts!")
            return count  # Return the number of attempts for this game

    print(f"Sorry, you've used all your attempts. The number was {num}.")
    return None  # Player didn't guess correctly

# Main Game Loop
highest_score = None  # Track the best (lowest) score

while True:
    attempts_used = play_game()
    
    if attempts_used is not None:  # If the player guessed correctly
        if highest_score is None or attempts_used < highest_score:
            highest_score = attempts_used
            print(f"New High Score: {highest_score} attempts!")
        else:
            print(f"Your score this game: {attempts_used} attempts. High Score: {highest_score} attempts.")

    # Ask the player if they want to play again
    replay = input("\nDo you want to play again? Enter 'yes' or 'no': ").strip().lower()
    if replay != 'yes':
        print("Thank you for playing! Goodbye!")
        print(f"Your highest score was: {highest_score if highest_score is not None else 'No score recorded'}")
        break
