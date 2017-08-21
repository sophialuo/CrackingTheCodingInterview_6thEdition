'''
Smallest K: Design an algorithm to find the smalelst K numbers in an array
'''

import heapq
def smallest_k(lst, K):
	if len(lst) <= K:
		return lst

	sublst = lst[:K] 
	heapq._heapify_max(sublst)

	for i in range(K, len(lst)):
		if lst[i] < sublst[0]:
			sublst[0] = lst[i]
			heapq._heapify_max(sublst) 

	print(sublst)


	print(sublst)

lst = [1, 4, 3, 5, 8, 9, 1, 12, 13]
K = 5
print(smallest_k(lst, K))