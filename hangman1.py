target_word = 'коробка'
tries = 6
guessed_letters = []


def is_word(x):
    return len(x) > 1


def get_input():
    while True:
        letter_or_word = input()
        if is_word(letter_or_word):
            return letter_or_word

        if letter_or_word not in guessed_letters:
            break

    return letter_or_word


while tries > 0:
    word_or_letter = get_input()

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
    print("dead end")