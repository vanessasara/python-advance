import random,time,json

def basic_ques():
    with open('math_basic.json','r') as f:
        result = json.load(f)
    random_ques = random.choice(result)

    question_bas = random_ques['question']
    answer_bas = random_ques['answer']
    return question_bas, answer_bas

question_bas, answer_bas = basic_ques()

def intermediate_ques():
    with open('math_intermediate.json','r') as f:
        ques = json.load(f)
    random_ques = random.choice(ques)

    question_in = random_ques['question']
    answer_in = random_ques['answer']
    return question_in, answer_in

question_in, answer_in = intermediate_ques()

def advance_ques():
    with open('math_advance.json','r') as f:
        res = json.load(f)
    random_ques = random.choice(res)

    ques_adv = random_ques['question']
    ans_adv = random_ques['answer']

    return ques_adv , ans_adv

ques_adv , ans_adv = advance_ques()

TOTAL_QUES = 10
score = 0
wrong = 0
start_time = time.time()
input('Press enter to start the game! ')
print('<-------------------------------->')

user_level = input('\nEnter the level of math question you want: (basic/int/adv) ').lower()

for _ in question_bas, question_in, ques_adv:
    while True:
        if user_level == 'basic':
            asking_adv_ques = input('problem ' + ' ' + question_bas + '= ')
            if asking_adv_ques == answer_bas :
                score += 1
                break
            wrong += 1

        elif user_level == 'int':
            asking_adv_ques = input('problem ' + ' ' + question_in + '= ')
            if asking_adv_ques == answer_in :
                score += 1
                break
            wrong += 1

        elif user_level == 'adv':
            asking_adv_ques = input('problem ' + ' ' + ques_adv + '= ')
            if asking_adv_ques == ans_adv :
                score += 1
                break
            wrong += 1

        else:
            break

end_time = time.time()
total_time = round(end_time - start_time,2)

print('<-------------------------------->')
print('Greak Work! You took ',total_time, 'seconds!!!!')
print('<-------------------------------->')
print('Your total score is:',score)