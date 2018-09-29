import json
from difflib import get_close_matches
from difflib import SequenceMatcher
data = json.load(open("data.json"))
word = input('Please enter a word: ')
word = word.lower()
def return_def(word_predicted,word):
    if word_predicted :
        if word_predicted !=[None] and SequenceMatcher(None,word,word_predicted[0]).ratio() == 1:
            for i in data[word_predicted[0]]:
                print (i)
        else:
            print(f'Are you trying to type {word_predicted[0]}')
    else:
        print('Please enter a correct word')
word_predicted = get_close_matches(word,data.keys(),n=1,cutoff = .7)
return_def(word_predicted,word)