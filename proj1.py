print("Welcome to my quiz game!")


name = input('Please enter your name: ')
playing = input('Do you wanna play? ')

options = ['artificial intelligence',
'large language model','assistant','central processing unit','user interface']
score = 0


if playing.lower() != 'yes':
    quit()
else:
    print(f'Welcome {name} to quiz game ')

answer = input('What does AI means? \nA. Artificial intelligence\nB. Argo integration\nC. Animation Interface\nD.None\n')
if answer.lower() == 'artificial intelligence' in options:
    score += 1
    print("Correct!!!")
else:
    print('Incorrect :(')


answer = input('What does a LLm means? \nA. Chatgpt\nB. Large language model\nC. lambda functions\nD.ALL OF ABOVE\n')
if answer.lower() == 'large language model' in options:
    score += 1
    print("Correct!!!")
else:
    print('Incorrect :(')


answer = input('Agent is like an? \nA. Assitant\nB. User interface\nC. Global warn\nD.None\n')
if answer.lower() == 'assistant' in options:
    score += 1
    print("Correct!!!")
else:
    print('Incorrect :(')


answer = input('What does CPU stands for? \nA. ArgoCD\nB. Devops\nC. Animation Interface\nD.central processing unit\n')
if answer.lower() == 'central processing unit' in options:
    print("Correct!!!")
    score += 1
else:
    print('Incorrect :(')


answer = input('what is UI? \nA. Artificial intelligence\nB. Animation\nC. user interface\nD.All of above\n')
if answer.lower() == 'user interface' in options:
    score += 1
    print("Correct!!!")
else:
    print('Incorrect :(')

print(f'Your Total correct answers is {score} ')
print('Your percentage is ' + str((score/5) * 100))