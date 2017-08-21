'''
T9: On old cell phones, users typed on a numeric keypad and the phone would provide a list of words that matched these numbers. Each
digit mapped to a set of 0-4 leters. Impelment an algorithm to return a list of matching words, given a sequence of digits. You are
provided a list of valid words (provided in whatever data structure you'd like). 

1: None
2: abc
3: def
4: ghi
5: jkl
6: mno
7: pqrs
8: tuv
9: wxyz
0: None

Example
Input: 8733
Output: tree, used
'''
import itertools
# list(itertools.product(*a))

valid_words = [] #some list of valid words
mapping = {1: None, 2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv'}

def t9(digits):
	lst = []
	while digits != 0:
		num = digits % 10
		digits = int(digits/10)
		possible = list(mapping[num])
		lst.append(possible)
	lst = reversed(lst)

	all_words = list(itertools.product(*lst))
	''' 
	#uncomment for results when given valid_words
	actual_words = []
	if all_words in valid_words:
		actual_words.append(all_words)
 	
	return actual_words
	'''
	return all_words

print(t9(8733))


