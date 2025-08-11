
user_amount = input('Please enter your monthly income: $')
def total_income():

    while True:
        if user_amount.isdigit():
            user_amountt = int(user_amount)
            if user_amountt <= 0:
                print('Please enter an amount greater than 0.')
                break
            else:
                print(f"Let's calculate your monthly expense")
                break
        else:
            print('Please enter a valid amount.')

total_income()

category = input('What are your expenses (bills/tax)')
