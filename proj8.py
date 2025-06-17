import random

username = input('Welcome to ABC bank account\nEnter your username to log in: ')
password = input('Enter your Password to log in: ')

balance = random.randint(1000,10000)

def pass_reset():
    new_pass = input('\nEnter your new password: ')
    with open('user_pass.txt','r+') as f :
        content = f.read()
        target = "|"
        after_index = content.find(target)
        if after_index != -1:
            after = content[after_index + len(target):]
            modified_after = after.replace('\nhello', new_pass,1)
            new_content = content[:after_index + len(target)] + modified_after
            f.write(new_content)
        else:
            print("Character not found")
        print(f'\nYou changed your password from {content} to {new_pass}')
        



while True:
    with open('user_pass.txt', 'r') as f:
        user_check = f.read().strip()
        stored_username, stored_password = user_check.split('|') 

    if username != stored_username and password != stored_password:
        print('\nInvalid credentials! :(')
        break
    else:
        print('\nLoggedIn successfully!! ☺')
        break

while True:
    user_query = input('\nDo you want to reset your password Or check your balance? (p/b): ')
    if user_query == 'b':
        print('Your current balance is',balance)
        print('Thank you for chosing our service :)')
        break
    elif user_query == 'p':
        pass_reset()
        break
    else:
        break