'''
17.18
Shortest Supersequence: You are given two arrays, one shorter (with all distinct elements) and one longer. Find the shortest subarray
in the longer array that contains all the elements in the shorter array. The items can appear in any order

EXAMPLE
INPUT: {1, 5, 9} | {7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7}
output: [7, 10]
'''
#rolling window solution
def shortest_supersequencce(elems, lst):
	#create window
	start = 0
	while lst[start] not in elems:
		start += 1
	discovered = {}
	discovered[lst[start]] = 1
	end = start+1
	while len(discovered) != len(elems):
		if lst[end] in elems:
			if lst[end] in discovered:
				discovered[lst[end]] += 1
			else:
				discovered[lst[end]] = 1
		end += 1

	end -= 1 #index is one off
	shortest = end-start
	cur_indices = (start, end)

	#sliding window
	while end < len(lst):
		index = start+1
		if index >= len(lst):
			return cur_indices

		discovered[lst[start]] -= 1
		missing = lst[start]

		if is_done(discovered):
			start += 1
			shortest = end-start
			cur_indices = (start, end)
		else:
			while index < len(lst) and lst[index] not in elems:
				index += 1

			if index >= len(lst):
				return cur_indices

			start = index

			while end < len(lst) and lst[end] != missing:
				end += 1

			if end >= len(lst):
				return cur_indices

			discovered[lst[end]] += 1

			if end-start < shortest:
				shortest = end-start
				cur_indices = (start, end)
			

	return cur_indices


def is_done(discovered):
	for num in discovered:
		if discovered[num] == 0:
			return False
	return True

elems = {1, 5, 9}
lst = [7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7]
print(shortest_supersequencce(elems, lst))