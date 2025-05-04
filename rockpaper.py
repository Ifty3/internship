import random

def play_game():
    choices = ['rock', 'paper', 'scissors']
    computer = random.choice(choices)
    player = input("Enter your choice (rock, paper, scissors): ").lower()

    if player not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return

    print(f"Computer chose: {computer}")

    if player == computer:
        print("It's a tie!")
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        print("You win!")
    else:
        print("You lose!")

play_game()
