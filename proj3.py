import random

fruits_list = ['apple','mango','grapes']

random_fruit_guess = random.randint(0,2)
computer_guess = fruits_list[random_fruit_guess]

user_wins = 0
computer_wins = 0

while True:

    user_guess = input('Guess the fruits. \nOptions: \n1. Apple\n2. Mango\n3. Grapes\n')
    
    if user_guess == 'apple' and computer_guess == 'apple':
     user_wins += 1
     print('you got that right!')
     break

    elif user_guess == 'mango' and computer_guess == 'mango':
       user_wins += 1
       print('you got that right!')
       break

    elif user_guess == 'grapes' and computer_guess == 'grapes':
       user_wins +=1
       print('you got that right!')
       break

    else:
       computer_wins += 1
       print('You got that wrong :(')

if user_wins > computer_wins:
   print(f'user won by {user_wins} points and computer got {computer_wins}points.')

else:
   print(f'computer won by {computer_wins} points and user got {user_wins} points.')