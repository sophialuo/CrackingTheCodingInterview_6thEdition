'''
Sorted Merge: You are given two sorted arrays, A and B, where A has a lage enough buffer at the end to hold B.
Write a method to merge B into A in sorted order
'''

def sorted_merge(A, B):
	indexA = 0
	while A[indexA] != '':
		indexA += 1
	indexA -= 1 #overshoots by 1
	indexB = len(B)-1
	cur_index = len(A)-1

	while indexB >= 0:
		elemA, elemB = A[indexA], B[indexB]
		if elemB > elemA:
			A[cur_index] = elemB
			indexB -= 1
		else:
			A[cur_index] = elemA
			indexA -= 1

		cur_index -= 1

	return A

A = [1, 3, 5, 7, 9, '', '', '', '']
B = [2, 4, 6, 8]

print(sorted_merge(A, B))