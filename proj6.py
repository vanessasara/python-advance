import random

shuffle_list = [0,25,50,100]
random.shuffle(shuffle_list)
player_role = ['chor','sepahi','wazeer','badshah']

print(shuffle_list)

while True:
    print('Badshah badshah ka wazeer kon? ')
    for i in shuffle_list:
        if shuffle_list[i] == 50:
            print(shuffle_list)
    break




    
