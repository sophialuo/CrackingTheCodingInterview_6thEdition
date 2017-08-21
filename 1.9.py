'''
String Rotation: Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is a 
	             rotation of s1 using only one call to isSubstring (e.g., "waterbottle" is a rotation of erbottlewat")
'''

def isSubstring(s1, s2):
	if s1 in s2 or s2 in s1:
		return True
	return False

def string_rotation(s1, s2):
	if len(s1) != len(s2):
		return False
	
	for i in range(len(s1)):
		substr_front, substr_back = s1[:i], s1[i:]
		if isSubstring(substr_front, s2) and isSubstring(substr_back, s2):
			return True
	return False

#testing
string_pairs = [('waterbottle', 'erbottlewat'), ('a', 'aa'), ('aaa', 'aaa'), ('abc', 'bac')]
answers = [True, False, True, False]
count = 0

for i in range(len(string_pairs)):
	s1, s2, ans = string_pairs[i][0], string_pairs[i][1], answers[i]
	if string_rotation(s1, s2) == ans:
		print('correct')
		count += 1
	else:
		print('incorrect for test case: ' + str(string_pairs[i]))

if count == len(string_pairs):
	print('all correct!')