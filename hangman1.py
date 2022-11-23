import random

word_list = ['somebody', 'once', 'told', 'me', 'the', 'world', 'is', 'gonna', 'roll', 'me']

def get_word():
    return random.choice(word_list)
    
def print_word(word_, list_):
    for c in word_:
        if c in list_:
            print(c, end=' ')
        else:
            print('_', end=' ')
    print()
    

def play(word):
    word_completion = '_ ' * len(word)  
    guessed = False                    
    guessed_letters = []               
    guessed_words = []                 
    tries = 6                          
    print("Let's play!")
    print(display_hangman(tries))
    print(word_completion)
    while True:
        word_input = input('Enter a letter or word: ').upper()
        if not word_input.isalpha():
            print("it's not a letter, try again")
            continue
        if word_input in guessed_words or word_input in guessed_letters:
            print("this letter has already been")
            continue
        if len(word_input) > 1:
            if word_input == word:
                print('Congratulations! You won!')
                break
            else:
                guessed_words.append(word_input)
                tries -= 1
                print(f'Wrong, attempts left: {tries}')
                print(display_hangman(tries))
                print_word(word, guessed_letters)
                if tries == 0:
                    print(f'You failed to guess the word: {word}')
                    break
                continue



        if word_input in word:
            guessed_letters.append(word_input)
            for c in word:
                if c not in guessed_letters:
                    print('You guessed the letter')
                    print_word(word, guessed_letters)
                    guessed = False
                    break
                guessed = True
            if guessed:    
                print_word(word, guessed_letters)
                print('Congratulations! You won!')
                break
        else:
            guessed_letters.append(word_input)
            tries -= 1
            print(f'Wrong, attempts left: {tries}')
            print(display_hangman(tries))
            print_word(word, guessed_letters)
        if tries == 0:
            print(f'You failed to guess the word: {word}')
            break
            
    
def display_hangman(tries):
    stages = [
                '''
                _______
                |     |
                |     O
                |    \|/
                |     |
                |    / \
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
    return stages[tries]

play(get_word().upper())    
