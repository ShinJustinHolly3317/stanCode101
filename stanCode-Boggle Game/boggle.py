"""
File: boggle.py
Name: Justin (discussed with Tina)
----------------------------------------
TODO: This is a game to find any word constructed by adjacent(horizontally, vertically, and diagonally) letters, which are in a 4x4 array.
"""
import time


# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
dictionary = {}


def main():
	"""
	TODO: Find out all the possible combination of the word
	"""
	print('Welcome to boggle game!!')
	start = time.time()

	boggle_lst = []
	exist_words = []
	# String manipulation
	for i in range(1, 5):
		row = input(f'{i} row of letters: ')
		row_lst = row.split()
		boggle_lst.append(row_lst)
	read_dictionary(boggle_lst)
	search_word(boggle_lst, exist_words)
	print(f'There are {len(exist_words)} words in total.')
	end = time.time()
	# print(f'Total searching time:{end - start}')


def read_dictionary(boggle_lst):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:
			line = line.strip()
			for i in range(len(boggle_lst)):  # delete words with a starting letter that doesn't exist in the boggle
				if line[0] in boggle_lst[i]:
					dictionary[line] = True


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for key in dictionary:
		if key.startswith(sub_s):
			return True
	return False


def search_word(boggle_lst, exist_words):
	# Loop over the 16 boggle 'starting' alphabet
	for i in range(len(boggle_lst)):
		for j in range(len(boggle_lst[i])):
			no_repeat = [[i, j]]
			search_helper([boggle_lst[i][j]], no_repeat, boggle_lst, exist_words, i, j)


def search_helper(cur_str, no_repeat, boggle_lst, exist_words, i, j):
	# Answer case: find the answer but keep going deeper to find another
	if len(cur_str) >= 4 and ''.join(cur_str) in dictionary and ''.join(cur_str) not in exist_words:
		exist_words.append(''.join(cur_str))
		print(f'Found \"{"".join(cur_str)}\"!')

	# base case: no prefix
	elif not has_prefix(''.join(cur_str)) and len(cur_str) != 0:
		return

	# Recursion Case
	for m in range(i - 1, i + 2):
		for n in range(j - 1, j + 2):
			if 0 <= m < len(boggle_lst) and 0 <= n < len(boggle_lst):
				if [m, n] not in no_repeat:
					# Choose
					cur_str.append(boggle_lst[m][n])
					no_repeat.append([m, n])
					# Explore
					search_helper(cur_str, no_repeat, boggle_lst, exist_words, m, n)
					# Un-choose
					no_repeat.pop()
					cur_str.pop()


if __name__ == '__main__':
	main()
