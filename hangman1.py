import random

def get_word():
    with open('word_list.txt', 'r', encoding='utf-8') as file:
      word_list=file.read().split()
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


def play(target_word):
    tries = 6 
    guessed_letters = [] 
                         
    print("Let's play!")

    while tries > 0:

        print(display_hangman(tries))
        print_word(target_word, guessed_letters)

        word_or_letter = get_input(guessed_letters)

        if is_word(word_or_letter):
            word = word_or_letter

            if word == target_word:
                print('end')
                break
            else:
                tries -= 1
        else:
            letter = word_or_letter

            if letter in target_word:
                guessed_letters.append(letter)

                if set(target_word) == set(guessed_letters):
                    print("end")
                    break
            else:
                tries -= 1
                
    if tries == 0:
        print(display_hangman(0))
        print("dead end")


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
    return stages[tries_]


play(get_word().upper())  