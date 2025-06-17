import random

user_name = input('Welcome to ABC Bank.\nEnter your existing username or create one: ').lower()
balance = random.randint(1000,50000)

def user_add():
    new_user = input('write your user name: ')
    with open('username_manager.txt','a') as f:
                f.write('\n' + new_user )
    print(f'Welcome to your bank {new_user}')

     
def user_checking():
    with open('username_manager.txt', 'r') as f:
        users = [line.strip().lower() for line in f]  
        if user_name not in users:
            invalid_user = input('Type q to quite\nUser invalid!!. Do you want to create one (yes/no)? ').lower()
            if invalid_user == 'q':
                quit()
            if invalid_user == 'yes':
                user_add()
            else:
                print('Invalid option, write yes or no.')
                quit()
        else:
            print(f'Welcome to your bank {user_name}')

user_checking()

while True:
    user_query = input('type q to exit:\nDo you want to check your balance or change user name?\nType (balance/username):  ').lower()
    if user_query == 'q':
         break
    if user_query == 'username':
        new_username = input('Write your new user name: ').lower()
        with open('username_manager.txt', 'r+') as f:
            content = f.read()
            
            updated_content = content.replace(user_name, new_username)
            
            f.seek(0)
            f.write(updated_content)
            f.truncate()
        print(f'You changed your username from {user_name} to {new_username}')
        user_name = new_username
    
    elif user_query == 'balance':
         print(f'Your current balance is {balance} ')
         break
    else:
         print('Invalid option type (balance/username)')