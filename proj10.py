
def total_income():

    while True:
        user_amount = input('Please enter your monthly Expenses: $')
        if user_amount.isdigit():
            user_amount = int(user_amount)
            if user_amount <= 0:
                print('Please enter an amount greater than 0.')
            else:
                print(f'Your total amount is ${user_amount}')
                break
        else:
            print('Please enter a valid amount.')

def category():
    user_category = input('') 

            

def main():
    amount = total_income()

main()