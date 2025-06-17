import random
import time
import json

with open('math_ques.json','r') as f:
    result = json.load(f)


def calculate_prob():
    random_ques = random.choice(result)

    question = random_ques['question']
    answer = random_ques['answer']
    return question, answer

wrong = 0 
start_time = time.time()
input('Press Enter to start the game!')
print('------------------------')
print('Your time has started')

for i in range(10):
    question, answer = calculate_prob()
    while True:
        final_answer = input('Problem '+ str(i + 1)+': ' + question +' = ')
        if final_answer == str(answer):
            break
        wrong += 1 

end_time = time.time()
total_time = round(end_time - start_time,1)
print('------------------------')
print('Greak work , You finished in' , total_time,'seconds!')