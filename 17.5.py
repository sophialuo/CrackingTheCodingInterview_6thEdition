'''
Letters and Numbers: Given an aray filled with letters and numbers, find the longest subarray with an equal number of letters and numbers
'''

def letters_and_numbers(arr):
	numbers, letters, diff = [], [], []
	index = 0
	n, l = 0, 0
	diffIndices = {}
	while index < len(arr):
		if type(arr[index]) == int:
			n += 1
		else:
			l += 1
		
		letters.append(l)
		numbers.append(n)

		d = abs(l-n)
		diff.append(d)
		if d in diffIndices:
			if len(diffIndices[d]) == 1:
				diffIndices[d].append(index)
			else:
				diffIndices[d][1] = index 
		else:
			diffIndices[d] = [index+1]
	
		index += 1
	
	maxLen = 0
	indices = []
	for key in diffIndices:
		if len(diffIndices[key]) > 1 and  diffIndices[key][1] - diffIndices[key][0] > maxLen:
			maxLen = diffIndices[key][1] - diffIndices[key][0]
			indices = diffIndices[key]
	
	return indices


	


arr = ['a', 'a', 'a', 'a', 1, 1, 'a', 1, 1, 'a', 'a', 1, 'a', 'a', 1, 'a', 'a', 'a', 'a', 'a']
print(letters_and_numbers(arr))