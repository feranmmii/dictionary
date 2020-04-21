import json
from difflib import get_close_matches

with open('files/data.json') as dictionary:
    content = json.load(dictionary)


def translate(word):
    if word.lower() in content:
        return content[word.lower()]
    elif word.capitalize() in content:
        return content[word.capitalize()]
    elif word.upper() in content:
        return content[word.upper()]
    else:
        suggestion = get_close_matches(word, content.keys(), cutoff=0.8)
        if len(suggestion) > 0:
            while True:
                quest = input(f'do you mean "{suggestion[0]}"? \nEnter yes or no: ')
                if quest.lower() == 'yes':
                    return content[suggestion[0]]
                elif quest.lower() == 'no':
                    return 'The meaning of word you entered is not available'


def run_app():
    word = input('Enter a word: ')
    definition = translate(word)
    if definition is not None:
        return definition
    else:
        return 'please enter a correct English word'


data = run_app()
if type(data) == list:
    results = '\n'.join(data)
    print(results)
else:
    print(data)
