import json
from difflib import get_close_matches
from difflib import SequenceMatcher
data = json.load(open("data.json"))
ask = 'y'
def return_def(word_predicted,word):
    if word_predicted :
        if word_predicted and SequenceMatcher(None,word,word_predicted[0]).ratio() == 1:
            for i in data[word_predicted[0]]:
                print (i)
                return 'n'
        else:
            print(f'Are you trying to type {word_predicted[0]}')
            return input('Press y/n:')
    else:
        print('Please enter a correct word')
        
while ask.lower() == 'y':
    word = input('Please enter a word: ')
    word = word.lower()
    word_predicted = get_close_matches(word,data.keys(),n=1,cutoff = .750)
    opt = return_def(word_predicted,word)
    if opt.lower() == 'y' :
        return_def(word_predicted,word)
    ask = input('Do you wanna enter again y/n:')