import random

def roll():
    min_val = 1
    max_val = 6
    roll = random.randint(min_val, max_val)

    return roll

while True:
    player = input("Enter the number of players (2-4): ")
    if player.isdigit():
        player = int(player)
        if 2<=player<=4:
            break
        else:
            print("Number of players must be between 2-4.")
    else:
        print("Please enter a number.")

max_score = 50
player_score = [0 for _ in range(player)]

while max(player_score) < max_score:
    for player_idx in range(player):
        print(f"\nGet ready! Player {player_idx}, your turn has started.")
        print(f"Player {player_idx} your total score is {player_score[player_idx]}")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != 'y':
                break

            value = roll()
            if value==1:
                print("Oh no! You rolled a 1. No more rolls for you")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a {value}")

            print(f"Your score is {current_score}")

        player_score[player_idx] += current_score
        print(f"Your total score is {player_score[player_idx]}")

max_score = max(player_score)
winning_idx =  player_score.index(max_score)
print(f"Congrats Player {winning_idx+1}, you win!")