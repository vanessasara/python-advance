import random 

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbol_count = {
    '💗': 4,
    '✨': 7,
    '🌹': 5,
    '🎉': 8 
    }

def get_amount():
    while True:
        amount = input('Enter the amount of number: $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Please enter a valid value greater than 0. ')
        else:
            print('Please enter a numeric value')
    return amount

def number_of_lines():
    while True:
        lines = input('Enter the number of lines (1 - ' + str(MAX_LINES) +') ')
        if lines.isdigit():
            lines = int(lines)
            if MAX_LINES >= lines >= 1:
                break
            else:
                print(f'Please enter a valid value between 1 - {MAX_LINES} ')
        else:
            print('Please enter a numeric value')
    return lines

def lines_on_bet():
    while True:
        bet = input('How much you wanna bet on each line? $')
        if bet.isdigit():
            bet = int(bet)
            if bet > 0:
                break
            else:
                print('Please enter a valid value greater than 0. ')
        else:
            print('Please enter a numeric value')
    return bet

def get_bet_amount():
    while True:
        amount = input('Enter the amount of bet on each line: $')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'The amount must be between {MIN_BET} - {MAX_BET}.')
        else:
            print('Please enter a numeric value')
    return amount

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol_idx, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol_idx)

    columns = []
    for _ in range(cols):
        single_column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            random_value = random.choice(current_symbols)
            single_column.append(random_value)

        columns.append(single_column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()

symbol_value = {
    '💗': 4,
    '✨': 7,
    '🌹': 5,
    '🎉': 8 
    }

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def spin(balance):
    lines = number_of_lines()
    while True:
        bet = get_bet_amount()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    balance = get_amount()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


main()