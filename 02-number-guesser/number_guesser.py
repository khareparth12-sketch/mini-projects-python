import random
def guess_number(target, lower_bound=1, upper_bound=100):
    attempts = 0
    print(f"Here we go ! I'm thinking of a number between {lower_bound} and {upper_bound}. Can you guess it?")

    while True:
        try:
            guess = int(input("Go on take a guess: "))
            attempts += 1

            if guess<lower_bound or guess> upper_bound:
                print(f"Oh the number is between {lower_bound} and {upper_bound}. No worries, Try again!")
                continue
            if guess<target:
                print("Too low! Try again.")
            elif guess>target:
                print("Too high! Try again.")  
            else:
                print(f"Congratulations! You've guessed the number {target} in {attempts} attempts.")
                break
        except ValueError:
            print("No buddy that's not fair. Guess a Number!")

try:
    lower = int(input("Enter the lower bound of the range: "))
    upper = int(input("Enter the upper bound of the range: "))
    if lower>upper:
        print("No can do! The lower bound must be less than or equal to the upper bound.")
    else:
        num_to_guess = random.randomint(lower, upper)
        guess_number(num_to_guess, lower, upper)
except ValueError:
    print("Please type a number next time. Goodbye!")