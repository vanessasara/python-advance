import random


def roll():
    min_roll = 1
    max_roll = 6
    total_roll = random.randint(min_roll,max_roll)
    return total_roll


while True:
    players = input('Enter numbers of player (2-4): ')
    
    if players.isdigit():
        num_players = int(players)
        print(num_players)
        
        if 2 <= num_players <= 4:
          break
        else:
         print('Must be between 2 - 4')

    else:
     print('Invalid option')

max_score = 20 
players_score = [0 for _ in range(num_players)]

while max(players_score) < max_score:
    for player_idx in range(num_players):
        print('\nPlayer',player_idx +1 ,'has just started\n')
        current_score = 0
        while True:
            should_roll = input('Would you like to roll (y): ')
            if should_roll.lower() != 'y':
                break
            
            value = roll()
            if value == 1:
                print('You rolled 1 turn done')
                current_score = 0
                break
            else:
                current_score += value
                print('You rolled a:',value)
            print('You score is:',current_score)        
        
        players_score[player_idx] += current_score
        print('Your total score is:',players_score[player_idx])

max_score = max(players_score)
winning_idx  =players_score.index(max_score)
print('Player',winning_idx +1 ,'is the winner with the score of ',max_score)