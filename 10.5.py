'''
Sparse Search: Given a sorted array of strings that is interspersed with empty strings, write a method to find the
location of a given string.

EXAMPLE
Input: ball, {'at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', ''}
Output: 4
'''

def sparse_search(string, arr):
	start = find_next_right(arr, 0)
	end = find_next_left(arr, len(arr)-1)
	mid = find_next_right(arr, int((start+end)/2))

	while arr[mid] != string:
		if end <= start:
			return -1
		if string > arr[mid]:
			start = find_next_right(arr, mid+1)
		elif string < arr[mid]:
			end = find_next_left(arr, mid-1)
		mid = find_next_right(arr, int((start+end)/2))
	
	return mid

def find_next_left(arr, index):
	while arr[index] == '':
		index = index-1
	return index

def find_next_right(arr, index):
	while arr[index] == '':
		index = index+1
	return index


arr = ['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', '']
test_cases = [('at', 0), ('ball', 4), ('car', 7), ('dad', 10), ('hi', -1)]
counter = 0

for i in range(len(test_cases)):
	string, ans = test_cases[i]
	result = sparse_search(string, arr)
	if result == ans:
		counter += 1
		print("correct")
	else:
		print("incorrect for test case: " + str(test_cases[i]))

if counter == len(test_cases):
	print("all correct")