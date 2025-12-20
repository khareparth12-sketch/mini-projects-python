import random

COLORS = ["R", "B", "G", "P", "Y", "W", "O", "M"]
CODE_LENGTH = 4
TRIES = 10

def generate_code():
    code = []

    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)

    return code

def guess_code():
    while True:
        guess = input("Go on, try and guess the code: ").upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"You must guess all {CODE_LENGTH} colors")
            continue

        for color in guess:
            if color not in COLORS:
                print("Thats not right color, Try Again!")
                break
        else:
            break

    return guess

def check_code(guess, real_code):
    color_count = {}
    correct_pos = 0
    wrong_pos = 0

    for color in real_code:
        if color not in color_count:
            color_count[color] = 0
        color_count[color] += 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_code:
            correct_pos += 1
            color_count[guess_color] -= 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_count and color_count[guess_color] > 0:
            wrong_pos += 1
            color_count[guess_color] -= 1

    return correct_pos, wrong_pos

def game():
    print(f"Welcome to Mastermind, you have {TRIES} tries to guess the Code")
    print(f"Choose from following colors alone: ", *COLORS)

    code = generate_code()
    for attempts in range(1, TRIES+1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"Good Work! You guessed the code in {attempts} tries.")
            break

        print(f"Correct Positions: {correct_pos} | Incorrect Positons: {incorrect_pos}")

    else:
        print("Sorry, you ran out of tries. The code was: ", code)

if __name__ == "__main__":
    while True:
        print("Lets begin the game, press any key to start or 'q' to quit.")
        ans = input()
        if ans.lower() == 'q':
            break
        game()