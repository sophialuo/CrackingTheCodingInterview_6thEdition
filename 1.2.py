'''
Check Permutation: Given two strings, write a method to decide if one is a permutation of the other
'''

def check_permutation(str1, str2):
	if len(str1) != len(str2):
		return False
	
	count1, count2 = {}, {}
	for i in range(len(str1)):
		char1, char2 = str1[i],  str2[i]

		if char1 in count1:
			count1[char1] += 1
		else:
			count1[char1] = 1
		
		if char2 in count2:
			count2[char2] += 1
		else:
			count2[char2] = 1
	
	for char in count1:
		if char not in count2:
			return False
		if count1[char] != count2[char]:
			return False
	
	return True


#testing
str1 = ['aa', 'baa', 'cba', 'bbb', ' ', 'caa']
str2 = ['a', 'aba', 'abc', 'bbb', ' ', 'abc']
ans =  [False, True, True, True, True, False]
count = 0

for i in range(len(str1)):
	s1, s2, answer = str1[i], str2[i], ans[i]
	if check_permutation(s1, s2) != answer:
		print(check_permutation(s1, s2))
		print('incorrect for test case: ' + s1 + ', ' + s2)
	else:
		print('correct')
		count += 1

if count == len(str1):
	print('all correct!')