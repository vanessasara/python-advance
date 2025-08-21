import random

MAX_LINES = 3
COLS = 3
symbol_count = {
    '🧱': 10,
    '🗡': 7,
    '🛡': 5,
    '💎': 2 
    }

def amount_coins():
    while True:
        user_coins = input('Enter the amount of coins you wanna deposit: 💰')
        if user_coins.isdigit():
            user_coins = int(user_coins)
            if user_coins <= 0 :
                print('coins must be greater than 0.')
            else:
                break
        else:
            print('Amount must be numeric')

    return user_coins

def get_symbol():
    while True:
        symbol = input('Select the symbol you want to bet on: (1.🧱 2.🗡 3.🛡 4.💎) ')
        if symbol.isdigit():
            symbol = int(symbol)
            if symbol <= 0 :
                print('Please write a value greater than 0.')
            else:
                break
        else:
            print('Please write a numeric value')
    return symbol
         
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

def get_reward(cols,symbols):
    all_symbols = []
    for symbol_idx, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol_idx)

    columns = []
    for _ in range(cols):
        single_column = []
        current_symbol = all_symbols[:]
        for _  in range(3):
            random_value = random.choice(current_symbol)
            single_column.append(random_value)
        
        columns.append(single_column)

    return columns

def print_rewards(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != - 1:
                print(column[row], end=' | ')
            else:
                print(column[row], end='')
        
        print()

symbols_list = ['🧱','🗡','🛡','💎']

def check_winnings_reward(columns, lines, bet, values):
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
        bet = 10
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_reward(COLS, symbol_count)
    print_rewards(slots)
    winnings, winning_lines = check_winnings_reward(slots, lines, bet, symbols_list)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = amount_coins()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

main()