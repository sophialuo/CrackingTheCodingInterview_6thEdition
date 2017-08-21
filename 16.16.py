'''16.16 
Sub Sort: Given an array of integers, write a method to find indices m and n such that if you sorted
elements m through n, the entire array would be sorted. Minimize n-m (that is, find the smallest such
sequence)
EXAMPLE
Input: 1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19
Output: (3, 9)
'''

def subsort(lst):
	first, last = -1, -1
	for i in range(len(lst)-1):
		if lst[i] > lst[i+1]:
			first = i
			break
	for i in range(len(lst)-1, 0, -1):
		if lst[i] < lst[i-1]:
			last = i
			break

	min_unsorted, max_unsorted = min(lst[first:last+1]), max(lst[first:last+1])

	for i in range(len(lst)):
		if lst[i] > min_unsorted:
			first = i 
			break
	for i in range(len(lst)-1, -1, -1):
		if lst[i] < max_unsorted:
			last = i
			break
	
	return (first, last)

lst =  20, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19
print(subsort(lst))