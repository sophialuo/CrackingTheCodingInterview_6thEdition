'''
One Away: There are three types of edits that can be performed on strings: insert a character, remove a character,
or replace a charcater. Given two strings, write a function to check if they are one edit (or zero edits) away.

EXAMPLE
pale, ple --> true
pales, pale --> true
pale, bale --> true
pale, bake --> false
'''

def one_away(str1, str2):
	lendiff =  abs(len(str1) - len(str2))
	if lendiff >= 2:
		return False

	#make str1 be the larger string 
	if len(str1) < len(str2):
		temp = str1
		str1 = str2
		str2 = temp

	#remove a character, insert a character
	if lendiff == 1:
		for i in range(len(str1)):
			removed = str1[:i] + str1[i+1:]
			if str2 == removed:
				return True
		return False
	#replace a character
	else:
		for i in range(len(str1)):
			replaced1 = str1[:i] + str1[i+1:]
			replaced2 = str2[:i] + str2[i+1:]
			if replaced1 == replaced2:
				return True
		return False

#testing
string_pairs = [('pale', 'ple'), ('pales', 'pale'), ('pale', 'bale'), ('pale', 'bake')]
answers = [True, True, True, False]
count = 0

for i in range(len(answers)):
	str1, str2, ans = string_pairs[i][0], string_pairs[i][1], answers[i]
	if one_away(str1, str2) == ans:
		print('correct')
		count += 1
	else:
		print('incorrect for test case: ' + str(string_pairs[i]))

if count == len(answers):
	print('all correct!')
	