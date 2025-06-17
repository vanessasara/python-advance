with open('story.txt','r') as f:
    story = f.read()

words = set()
num = -1
start_of_word = '{'
end_of_word = '}'

for i,char in enumerate(story):
    if char == start_of_word:
       num = i

    if char == end_of_word and num != -1:
        word = story[num: i + 1]
        words.add(word)
        num = -1


answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)