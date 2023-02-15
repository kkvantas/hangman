import random
import requests
import json
import os
import re
import argparse


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
