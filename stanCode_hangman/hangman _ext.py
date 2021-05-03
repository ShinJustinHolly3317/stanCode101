"""
File: hangman.py
Name: Justin Kao__(discussed with Tina)
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This function will show a secret word, only showing the number of letters of a word.
    You has only 7 chances of wrong guesses.
    When right guess, it'll show on secret word.
    When wrong guess, the man in the picture is going to be hung on the guillotine step by step.
    """
    print("\n\n========HangMan Game========\n\n")
    ans = random_word()
    game_start(ans)
    print("The word was:", ans)


def game_start(ans):
    """
    1. Guess a character, if correct, show it.
        if wrong, HP minus 1.
    2. 2 endings:
        -get congrats when finding out the answer within N_TURNS wrong guess.
        -You'll be dead if running out of HP.
    :param ans: real word
    :return: None
    """
    progress = secret(ans)  # At first, need to cover the real word by "-".
    guess = ""
    hp = N_TURNS
    while not progress == ans:
        guillotine(hp)  # Display the hangman picture.
        print("The word looks like:", progress)
        print("You have", hp, "guesses left.")
        guess = input("Your guess: ")
        guess = guess.upper()
        if guess in ans:
            progress = display_progress(ans, guess, progress)
            print("\n\n====You are correct!====")
        else:
            if guess.isalpha() and len(guess) == 1:
                hp -= 1
                print("\n\n===There is no", guess + "'s in the word===")
                if hp == 0:  # You are dead.
                    print("\n\n====You are completely hung :(====")
                    guillotine(hp)
                    return  # get out of game_start() and return None.
            else:
                print("Illegal format!")
    print("You win!")  # Win the game.


def display_progress(ans, guess_ch, old_progress):
    """
    1. At first, compare 'guess_ch' with each character in 'ans', if matched, add it into 'new_progress'.
    2. Next round you'll have a 'old_progress' and a new 'guess_ch', add them together.
    :param ans: the real word
    :param guess_ch: the character guessed in this round
    :param old_progress: the progress in previous round
    :return: new_progress which adding old and new progress
    """
    new_progress = ""
    for i in range(len(ans)):
        if ans[i] == guess_ch or ans[i] == old_progress[i]:
            new_progress += ans[i]
        else:
            new_progress += "-"
    return new_progress


def secret(ans):
    """
    Make a variable showing "-" which covers the real word
    :param ans: the real word
    :return: a word covered by "-"
    """
    s = ""
    for ch in ans:
        s += "-"
    return s


def guillotine(hp):
    glltn1 = "\n\n\n" \
             "============="
    glltn2 = "||"
    glltn3 = "||"
    glltn4 = "||"
    glltn5 = "||"
    glltn6 = "||"
    glltn7 = "_____________\n" \
             "|           |\n" \
             "_____________"
    rope = "           |"
    head = "           0"
    l_hand = "          \\"
    r_hand = " /"
    belly = "           |"
    l_leg = "          /"
    r_leg = " \\"
    if hp == 6:
        glltn2 += rope
    elif hp == 5:
        glltn2 += rope
        glltn3 += head
    elif hp == 4:
        glltn2 += rope
        glltn3 += head
        glltn4 += l_hand
    elif hp == 3:
        glltn2 += rope
        glltn3 += head
        glltn4 += l_hand+r_hand
    elif hp == 2:
        glltn2 += rope
        glltn3 += head
        glltn4 += l_hand + r_hand
        glltn5 += belly
    elif hp == 1:
        glltn2 += rope
        glltn3 += head
        glltn4 += l_hand + r_hand
        glltn5 += belly
        glltn6 += l_leg
    elif hp == 0:
        glltn2 += rope
        glltn3 += head
        glltn4 += l_hand + r_hand
        glltn5 += belly
        glltn6 += l_leg+r_leg
    print(glltn1, glltn2, glltn3, glltn4, glltn5, glltn6, glltn7, sep="\n")


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"







#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
