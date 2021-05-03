"""
File: anagram.py
Name: Justin
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""
import time

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

dic_lst = []
# dic_lst = {}  # the other method, read all the vocabulary in 'dict'
check_lst = []


def main():
    """
    Todo: Find all the different rearrangement of the input word
    """
    print('Welcome to stanCode \"Anagram Generator\"! (or -1 to quit)')

    while True:
        s = input('Find anagrams for: ')
        if s == EXIT:
            print('Have fun!')
            break
        else:
            # set up list of searching results
            permutation_lst = []

            # execute search
            start_time = time.time()  # calculate searching time
            read_dictionary(s)
            find_anagrams(s)
            end_time = time.time()  # calculate searching time
            print(f'Searching time of "{s}": {end_time - start_time}')


def read_dictionary(s):
    """
    Todo: Read all the vocabulary as a list
    """
    lens = len(s)
    with open(FILE, 'r') as f:
        for line in f:
            line = line.strip()
            if len(line) == lens:  # Read only the same length
                dic_lst.append(line)

            ## the other method, read all the vocabulary in 'dict'
            # dic_lst[line] = ''


def find_anagrams(s):
    """
    Todo: use recursion to find all the anagram by helper
    :param s: input word
    """

    permutation_lst = []
    char_lst = []
    non_exist_lst = []
    num_lst = [i for i in range(len(s))]
    find_anagrams_helper(s, len(s), [], num_lst, permutation_lst, char_lst, non_exist_lst)
    print(f'{len(permutation_lst)} anagrams: {permutation_lst}')


def find_anagrams_helper(s, s_len, current_lst, num_lst, permutation_lst, char_lst, non_exist_lst):
    """
    Todo: Use digit order to find all the combination by recursion, meanwhile translate the order into alphabet
    :param s: input word: string
    :param s_len: length of input word
    :param current_lst: the current combination list: list(element: numbers)
    :param num_lst: list show the initial order
    :param permutation_lst: final list: list(string)
    :param char_lst: the current combination list: list(element: string)
    :param non_exist_lst: list can terminate recursion early: list(element: alphabet)
    :return: Recursion
    """
    # Check if this sub_s in non_exist_lst
    if char_lst in non_exist_lst:
        # print(char_lst)  # checking early termination of recursion
        return
    # Check this sub_s exist or not
    elif len(char_lst) > 1:
        if not has_prefix(char_lst):
            non_exist_lst.append(list(char_lst))
            return

    # create a order number to track the permutation
    if len(current_lst) == s_len:
        if has_prefix(char_lst):
            now_word = ''
            for char in char_lst:
                now_word += char
            if now_word in dic_lst and now_word not in permutation_lst:
                permutation_lst.append(now_word)
                print('Found:' + now_word)
                print('Searching......')
    else:
        for num in num_lst:
            if num in current_lst:
                pass
            else:
                # Choose
                current_lst.append(num)
                char_lst.append(s[num])
                # Explore
                find_anagrams_helper(s, s_len, current_lst, num_lst, permutation_lst, char_lst, non_exist_lst)
                # Un-choose
                char_lst.pop()
                current_lst.pop()


def has_prefix(char_lst):
    """
    Todo: Compare this sub_string exist or not
    :param char_lst: current sub_str: list(alphabet)
    :return: if exist, return True, else return False
    """
    now_word = ''
    for char in char_lst:
        now_word += char
    for vocabulary in dic_lst:
        if vocabulary.startswith(now_word):
            check_lst.append(char_lst)
            return True

    ## the other method, read all the vocabulary in 'dict'
    # for key, value in dic_lst.items():
    #     if key.startswith(now_word):
    #         check_lst.append(char_lst)
    #         print(char_lst)
    #         return True

    return False


if __name__ == '__main__':
    main()
