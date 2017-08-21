'''
17.21 
Volume of Histogram: Imagine a histogram (bar graph). Design an algorithm to compute the volume of water it could hold if someone
poured water across the top. You can assume that each historgram bar has width 1.
EXAMPLE
Input: 0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0}
Output: 26
'''

def volume_of_histograms(lst):
	prevBiggest, nextBiggest = [], []
	cur_biggest = 0
	for i in range(len(lst)):
		if lst[i] != 0:
			prevBiggest.append(cur_biggest)
			cur_biggest = max(cur_biggest, lst[i])
		else:
			prevBiggest.append(0)
		nextBiggest.append(0)
	cur_biggest = 0
	for i in range(len(lst)-1, -1, -1):
		if lst[i] != 0:
			nextBiggest[i] = cur_biggest
			cur_biggest = max(cur_biggest, lst[i])

	for i in range(len(lst)):
		if lst[i] != 0 and lst[i] < prevBiggest[i] and lst[i] < nextBiggest[i]:
			lst[i] = -lst[i]

	total = 0
	cur_num = 0
	counter = 0
	index = 0
	while index < len(lst):
		if lst[index] < 0:
			total += lst[index]

		if lst[index] != 0 and cur_num == 0:
			cur_num = lst[index]
		elif lst[index] > 0:
			total += min(lst[index], cur_num)*counter
			counter = 0
			cur_num = lst[index]
		elif lst[index] <= 0 and cur_num > 0:
			counter += 1
	

		index += 1


	return total

lst = [0, 0, 4, 0, 0, 6, 0, 0, 3, 1, 0, 5, 0, 1, 0, 0, 0]
print(volume_of_histograms(lst))
