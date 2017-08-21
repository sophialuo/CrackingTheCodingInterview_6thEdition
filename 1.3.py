'''
URLify: Write a method to replace all spaces in a string with '%20.' You may assume that the string has sufficient space at the end to hold the additional 
characters, and that you are given the "trye" length of the string.

EXAMPLE
Input: "Mr John Smith ", 13
Output: "Mr%20John%20Smith"
'''

def urlify(string):
	result = ''
	for char in string:
		if char == ' ':
			result += '%20'
		else:
			result += char
	return result

#testing
strings = ['   ', 'a a a', ' ', 'a', 'ab c', 'a  bc', 'abc']
answers = ['%20%20%20', 'a%20a%20a', '%20', 'a', 'ab%20c', 'a%20%20bc', 'abc']
count = 0

for i in range(len(strings)):
	string = strings[i]
	ans = answers[i]
	if urlify(string) == ans:
		print('correct')
		count += 1
	else:
		print('incorrect for test case: \'' + string + '\'')

if count == len(strings):
	print('all correct!')