'''
String Compression: Implement a method to perform basic string compression using the counts of repeated characters. For example, 
the string aabcccccaaa would become a2b1c5a3. If the compressed string would not become smaller than the original string, your
method should return the original string. you can assume the string has only uppercase and lowercase letters (a-z)
'''

def compress_string(string):
	index = 1
	count = 1
	char = string[0]
	result = char

	while index < len(string):
		if string[index] != char:
			result += str(count)
			char = string[index]
			result += char
			count = 1
		else:
			count += 1

		index += 1
	result += str(count)

	return result

#testing
strings = ['aabcccccaaa', 'AAaBbCCCcc', 'abcde', 'aaaa']
answers = ['a2b1c5a3', 'A2a1B1b1C3c2', 'a1b1c1d1e1', 'a4']
count = 0

for i in range(len(strings)):
	string, ans = strings[i], answers[i]
	if compress_string(string) == ans:
		count += 1
		print('correct')
	else:
		print('incorrect for test case: ' + string)

if count == len(strings):
	print('all correct!')