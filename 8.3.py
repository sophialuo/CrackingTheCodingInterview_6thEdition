'''
Magic Index: A magic index in an array A[0, ..., n-1] is defined to be an index such that 
A[i] = i. Given a sorted array of distinct integers, write a method to find a magic index,
if one exists, in array A

FOLLOW UP
What if the values are not distinct?
'''

def magic_index(arr):
	return magic_index_helper(arr, 0, len(arr)-1)

def magic_index_helper(arr, start, end):
	if end < start:
		return -1
	
	#get middle
	index = int((start+end)/2)
	print(index)
	val = arr[index]
	if index == val:
		return index

	#search left
	left = magic_index_helper(arr, start, min(index-1, val))
	if left >= 0:
		return left
	#search right
	right = magic_index_helper(arr, max(index+1, val), end)
	return right

arr = [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]
print(magic_index(arr)) #should return 2
