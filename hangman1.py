import get_word_modes



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
    get_word = get_word_modes.get_word_mode()
    play(get_word().upper())
except RuntimeError as e:
    print(e)
    exit(1)
