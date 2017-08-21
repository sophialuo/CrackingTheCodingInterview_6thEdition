'''
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome
is a word or phrase that is the same forwards and backwards. A pemutation is is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary word.

EXAMPLE
Input: Tact Coa
Output: True
'''

#algorithm: each character must appear an even number of times, only one character can appear an odd number of times
#		    a space is not considered a character
def palindrome_permutation(string):
	counts = {}
	for char in string:
		char = char.lower()
		if char != ' ':
			if char in counts:
				counts[char] += 1
			else:
				counts[char] = 1
	odd = 0
	for char in counts:
		if counts[char] %2 != 0:
			odd += 1
	
	if odd <= 1:
		return True
	return False

#testing
strings = ['Tact Coa', 'abcab', 'a', 'aa', 'ab', 'BbaaA', 'abcd']
answers = [True, True, True, True, False, True, False]
count = 0

for i in range(len(strings)):
	string, ans = strings[i], answers[i]
	if palindrome_permutation(string) == ans:
		print('correct')
		count += 1
	else:
		print('incorrect for test case: ' + string)

if count == len(strings):
	print('all correct!')
		