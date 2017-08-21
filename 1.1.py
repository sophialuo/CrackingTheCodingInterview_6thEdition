'''
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use a data structure?
'''

#with data structure
def is_unique(string):
	count = {}
	for char in string:
		if char in count:
			return False
		else:
			count[char] = 1
	return True

#without data structure 
def is_unique_v2(string):
	for i in range(len(string)):
		char = string[i]
		if char in string[i+1:]:
			return False
	return True


#testing
string1 = 'aaa' #should return False
string2 = 'abc' #should return True
string3 = 'aba' #should return False
string4 = 'a'   #should return True
string5 = 'aab' #should return False
string6 = 'baa' #should return False
lst = [string1, string2, string3, string4, string5, string6]
ans = [False, True, False, True, False, False]
version = 1

while version < 3: 
	count = 0
	if version == 1:
		print('with data structure')
	else:
		print('without data structure')

	for i in range(len(lst)):
		string = lst[i]
		answer = ans[i]

		if version == 1:
			if is_unique(string) == answer:
				print('correct!')
				count += 1
			else:
				print('incorrect for test case: ' + string)
		else:
			if is_unique_v2(string) == answer:
				print('correct!')
				count += 1
			else:
				print('incorrect for test case: ' + string)

	if count == len(lst):
		print('all correct!')

	version += 1

