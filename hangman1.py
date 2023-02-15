import random
import requests
import json
import os
import argparse
import re


def get_word_mode():
    modes = {'api': get_word_api,
            'file': get_word_from_file,
            'insane': insane_mode,
             'wd': word_of_the_day
            }
    parser = argparse.ArgumentParser(description='Choose mode')
    parser.add_argument('-m', '--mode', type=str, choices=list(modes.keys()), default='api', help='Choose mode: api - to get word from API; file - to get word from txt file, insane - insane mode, wd - word of the day')
    args = parser.parse_args()
    return modes[args.mode]

def word_of_the_day():
    wd_url = 'https://www.dictionary.com/e/word-of-the-day/'
    response = requests.get(wd_url)
    match = re.search(r'<h1 class="js-fit-text" style="color: #\S{6}">(\w+)</h1>', response.text)
    if match is None:
        raise RuntimeError('Sorry, original source has been changed, pls try other mode')
    return match.group(1)



def get_word_api():
    if 'RANDOM_WORD_API_KEY' not in os.environ:
        raise RuntimeError('API key is not set')
    api_key = os.environ['RANDOM_WORD_API_KEY']
    api_url = 'https://api.api-ninjas.com/v1/randomword'
    response = requests.get(api_url, params={'type': 'noun'}, headers={'X-Api-Key': api_key})
    output = json.loads(response.text)
    return output['word']


def insane_mode():
    api_url = 'https://www.thisworddoesnotexist.com/api/random_word.json'
    response = requests.get(api_url)
    output = json.loads(response.content)
    return output['word']['word']


def get_word_from_file():
    with open('word_list.txt', 'r', encoding='utf-8') as file:
        word_list = file.read().split()
    return random.choice(word_list)


def print_word(word_, list_):
    for c in word_:
        if c in list_:
            print(c, end=' ')
        else:
            print('_', end=' ')
    print()


def is_word(x):
    return len(x) > 1


def get_input(guessed_letters):
    while True:

        letter_or_word = input('Enter a letter or word: ').upper()

        if not letter_or_word.isalpha():
            print("it's not a letter, try again")
            continue

        if is_word(letter_or_word):
            return letter_or_word

        if letter_or_word not in guessed_letters:
            break
        else:
            print("this letter has already been")

    return letter_or_word


def display_end(tries, target_word):
    display_hangman(tries)
    print_word(target_word, target_word)
    if tries == 0:
        print('Dead end')
    else:
        print('Congrats')


def play(target_word):
    tries = 6
    guessed_letters = []

    print("Let's play!")

    while tries > 0:
        display_hangman(tries)
        print_word(target_word, guessed_letters)

        word_or_letter = get_input(guessed_letters)

        if is_word(word_or_letter):
            word = word_or_letter

            if word == target_word:
                break
            else:
                tries -= 1
        else:
            letter = word_or_letter

            if letter in target_word:
                guessed_letters.append(letter)

                if set(target_word) == set(guessed_letters):
                    break
            else:
                tries -= 1

    display_end(tries, target_word)


def display_hangman(tries_):
    stages = [
                '''
                _______
                |     |
                |     O
                |    \|/
                |     |
                |    / \\
                |
                |  oopsy
                
                ''',
                '''
                _______
                |     |
                |     O
                |    \|/
                |     |
                |    / 
                |  
                ''',
                '''
                _______
                |     |
                |     O
                |    \|/
                |     |
                |    
                |  
                ''',
                '''
                _______
                |     |
                |     O
                |    \|
                |     |
                |    
                |  
                ''',
                '''
                _______
                |     |
                |     O
                |     |
                |     |
                |     
                |  
                ''',
                '''
                _______
                |     |
                |     O
                |    
                |     
                |    
                |  
                ''',
                '''
                _______
                |     |
                |     
                |    
                |       
                |  
                '''
    ]
    print(stages[tries_])


try:
    get_word = get_word_mode()
    play(get_word().upper())
except RuntimeError as e:
    print(e)
    exit(1)
