import random

user_score = 0
comp_score = 0
choices = ['rock', 'paper', 'scissor']
win_mssg = ["Damn! You are on fire", "Winning Streak", "You're pro at this"]
win = ""

print("Welcome! Let's play Rock, Paper, Scissor.")
# print("How many rounds would you like to play?")
# rounds = int(input())

while True:
    print("Enter 'rock', 'paper', or 'scissor' to play. Type 'exit' to quit the game.")
    user_input = input("").lower()
    if user_input == "exit":
        print("Thanks for playing! Goodbye!")
        break

    if user_input not in choices:
        print("Wrong input. Choose from rock, paper, or scissor.")
        break

    comp_choice = random.choice(choices)
    print(f"Computer Choice: {comp_choice}")

    if user_input==comp_choice:
        print("Oh! It's a tie.\n")
        win = ""
        continue

    if user_input=='rock' and comp_choice=='scissor':
        if user_score>1 and win=="user":
            print(random.choice(win_mssg) + "\n")
        else:
            print("yay! You won!\n")
        win = "user"
        user_score+=1
    elif user_input=='scissor' and comp_choice=='paper':
        if user_score>1 and win=="user":
            print(random.choice(win_mssg) + "\n")
        else:
            print("yay! You won!\n")
        win = "user"
        user_score+=1
    elif user_input=='paper' and comp_choice=='rock':
        if user_score>1 and win=="user":
            print(random.choice(win_mssg) + "\n")
        else:
            print("yay! You won!\n")
        win = "user"
        user_score+=1
    else:
        win = "comp"
        print("You lost, Better Luck next Time.\n")
        comp_score+=1

print(f"User Wins: {user_score}\nComputer Wins: {comp_score}")