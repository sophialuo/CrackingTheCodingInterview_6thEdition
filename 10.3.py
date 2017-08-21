'''
Search in Rotated Array: Given a sorted array of n integers that has been rotated an unknwon numbe of times,
write code to find an element in the array. You may assume that the array was originally sorted in
increasing order.
'''

def search_helper(start, end, arr, num):
	mid = int((start+end)/2)

	if arr[mid] == num:
		return mid
	if arr[start] == num:
		return start
	if arr[end] == num:
		return end
	if start+1 == mid and mid+1 == end:
		return -1
	

	#find the normally ordered side
	if arr[mid] <= arr[end]:
		if num > arr[mid] and num < arr[end]:
			return search_helper(mid, end, arr, num)
		else:
			return search_helper(start, mid, arr, num)
	elif arr[start] <= arr[mid]:
		if num > arr[start] and num < arr[mid]:
			return search_helper(start, mid, arr, num)
		else:
			return search_helper(mid, end, arr, num)


def search_rotated_array(arr, num):
	return search_helper(0, len(arr)-1, arr, num)


arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
test_cases = [(15, 0), (19, 2), (25, 4), (1, 5), (5, 8), (14, 11), (27, -1)]
counter = 0

print("Searching in: " + str(arr))
for i in range(len(test_cases)):
	num, ans = test_cases[i]
	result = search_rotated_array(arr, num)

	if result == ans:
		counter += 1
		print("correct")
	else:
		print(result)
		print("incorrect for test case: " + str(test_cases[i]))

if counter == len(test_cases):
	print("all correct")