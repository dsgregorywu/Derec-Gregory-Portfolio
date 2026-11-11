#################################################################
# Name: Derec
# Collaborators (none):
# Generative AI transcript link (if any):
# Estimated time spent (hr): 5
# Description of any added extensions:
#################################################################

from WordleGraphics import WordleGWindow, N_ROWS, N_COLS
from english import ENGLISH_WORDS, is_english_word
from WordleGraphics import CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
import random
import english

def wordle():
    """ The main function to play the Wordle game. """
    gw = WordleGWindow()
    secretwordlength = 0
    while secretwordlength != N_COLS:
        randomword = random.choice(ENGLISH_WORDS)
        secretwordlength = len(randomword)
    secret_word = ""
    secret_word += randomword
    grayletters = list()
    yellowletters = list()
    greenletters = list()
    def enter_action():
        guessnumber = gw.get_current_row()
        colnumb = 0
        colnumbguess = 0
        guessed_word = str("")
        for col in range(N_COLS):
            letter = gw.get_square_letter(guessnumber, colnumbguess)
            guessed_word += letter.lower()
            colnumbguess += 1
        letter_counts = {}
        for letter in secret_word:
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1
        used_cols = [False] * N_COLS
        if guessed_word in ENGLISH_WORDS and len(guessed_word) == N_COLS:
            for col in range(N_COLS):
                letter = gw.get_square_letter(guessnumber, colnumb)
                letter = letter.lower()
                if letter == secret_word[col]:
                    gw.set_square_color(guessnumber, col, CORRECT_COLOR)
                    used_cols[col] = True
                    letter_counts[guessed_word[col]] -= 1
                    colnumb += 1
                    greenletters.append(letter)
                    gw.set_key_color(letter, CORRECT_COLOR)
                else:
                    colnumb += 1
            colnumb = 0
            for col in range(N_COLS):
                letter = gw.get_square_letter(guessnumber, colnumb)
                letter = letter.lower()
                if not used_cols[col] and letter in letter_counts and letter_counts[letter] > 0:
                    gw.set_square_color(guessnumber, col, PRESENT_COLOR)
                    used_cols[col] = True
                    letter_counts[letter] -= 1
                    colnumb += 1
                    yellowletters.append(letter)
                    if not letter in greenletters:
                        gw.set_key_color(letter, PRESENT_COLOR)
                else:
                    colnumb += 1
            colnumb = 0
            for col in range(N_COLS):
                letter = gw.get_square_letter(guessnumber, colnumb)
                letter = letter.lower()
                if not used_cols[col]:
                    gw.set_square_color(guessnumber, col, MISSING_COLOR)
                    grayletters.append(letter)
                    if letter not in greenletters and letter not in yellowletters:
                        gw.set_key_color(letter, MISSING_COLOR)
                    colnumb += 1
                else:
                    colnumb += 1
            guessnumber += 1
            if guessed_word == secret_word:
                gw.show_message("You win!")
            elif (guessnumber) == N_ROWS:
                gw.show_message("You lost! The word was " + secret_word)
            else:
                gw.set_current_row(guessnumber)
        else:    
            gw.show_message("Not in word list") 
    gw.add_enter_listener(enter_action)


# Startup boilerplate
if __name__ == "__main__":
    wordle()
