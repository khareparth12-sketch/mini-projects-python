import random

MAX_LINES = 3
MIN_BET = 5
MAX_BET = 100

ROWS = 3
COLS = 3
symbol_count ={
    "A" : 2,
    "B" : 4,
    "C" : 3,
    "D" : 5
}
symbol_value ={
    "A" : 5,
    "B" : 4,
    "C" : 2,
    "D" : 1
}

def get_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(column)-1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def check_wins(columns, lines, bet, values):
    winning = 0
    win_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winning += values[symbol]*bet
            win_line.append(line+1)

    return winning, win_line

def deposit():
    while True:
        print("What would you like to deposit?")
        amt = input("$")
        if amt.isdigit():
            amt = int(amt)
            if amt>0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter the amount in number.")

    return amt

def get_no_of_lines():
    while True:
        print(f"How many lines would you like to bet on (1 - {MAX_LINES})?")
        lines = input()
        if lines.isdigit():
            lines = int(lines)
            if 1<lines<MAX_LINES:
                break
            else:
                print(f"Number of Lines must be between 1 and {MAX_LINES}.")
        else:
            print("Please enter the number of lines in number.")

    return lines

def get_bet():
    while True:
        print("How much would you like to bet on each line?")
        amt = input("$")
        if amt.isdigit():
            amt = int(amt)
            if MIN_BET<amt<=MAX_BET:
                break
            else:
                print(f"Your bet must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter the amount in number.")

    return amt

def spin_it(balance):
    lines = get_no_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines

        if total_bet > balance:
            print(f"You do not have enough balance to place a bet. Your current balance is ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Your total betting amount is ${total_bet}")

    slots = get_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, win_lines = check_wins(slots, lines, bet, symbol_value)
    if winnings == 0:
        print("Sorry! Better Luck Next Time.")
    else:
        print(f"You win ${winnings}")
        print(f"You won on line {win_lines}")

    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Your current balance is ${balance}.")
        spin = input("Press enter to play or 'q' to quit. ")
        if spin.lower() == 'q':
            break
        balance += spin_it(balance)

    print(f"You left with ${balance}.")

main()