"""
File: hangman.py
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""


import random


# This constant controls the number of guess the player has
N_TURNS = 7
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    Function:   Plays hangman game.
    Principle:  Input letters, judge whether it is the answer,
                and make a corresponding response
                (answer correct > continue, answer incorrect > deduct blood)
                until all guesses are correct or the blood volume is zero.
    """
    ans = random_word()
    print(hand_game(ans) + '\nThe word was: ' + ans)


def hand_game(ans):
    '''
    Function: Execute until all guesses are correct or the blood volume is zero.
    :param ans: str,Answer word
    :return: str,Game result
    '''

    '''
    Initialization:
        hp: int,Can guess the number of wrong chances
        ans_len: int,Answer word count
        right_num: int,Number of correct words
        now_ans: str,Now answer (ex:____)
        log_guess: str,History answer
    '''
    hp = N_TURNS
    ans_len = len(ans)
    right_num = 0
    log_guess = ''
    now_ans = ''
    for i in range(ans_len):
        now_ans += '_'

    '''
    End conditions: 
        1. The number of guesses = number of letters. 
        2. HP returns to zero.
    '''
    while True:
        if right_num == ans_len:
            return 'You win!!'
        elif hp == 0:
            return 'You are completely hung : ('
        else:
            print('The word looks like: ' + now_ans)
            print('You have ' + str(hp) + ' guess left.')
            guess = input('Your guess: ').upper()

            # ALPHABET has all the letters, if there are none in it, it is abnormal.
            if ALPHABET.find(guess) == -1:
                print('<ERORR: Illegal format.>')
            else:
                # log_guess has all the historical answers, if there is, it is abnormal.
                if log_guess.find(guess) != -1:
                    print('<ERORR: You guess repeatedly>')
                else:
                    if ans.find(guess) == -1:
                        log_guess += guess
                        hp -= 1
                        print('There is no ' + guess + '\'s in the word.')
                    else:
                        log_guess += guess
                        for i in range(ans_len):
                            if ans[i] == guess:
                                now_ans = now_ans[:i] + guess + now_ans[i + 1:]
                                right_num += 1


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
