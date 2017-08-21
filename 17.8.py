'''
Circus Tower: A circus is designing a tower routine consisting of people standing atop one another's shoulder. For
practical and aesthetic reasons, each person must be both shorter and lighter than the person below him or her. 
Given the heights and weights of each person in the circus, write a method to compute the largest possible number
of people in such a tower.

EXAMPLE
Input (ht, wt): (65, 100) (70, 150) (56, 90), (75, 190), (60, 95), (68, 110)
Output: The longest tower is length 6 and includes from top to bottom:
(56, 90) (60, 95) (65, 100) (68, 110) (70, 150) (75, 190)
'''

def circus_tower(lst):
	sortedLst = sorted(lst, key = lambda x: (x[1], x[0]))
	
	cur_max = -1
	for i in range(len(lst)):
		computed = helper(i, sortedLst[i], sortedLst) + 1
		if len(lst)- i < computed: #not possible for there to be a longer sequence
			return cur_max
		if cur_max < computed:
			cur_max = computed

	return cur_max


def helper(index, cur, lst):
	if index == len(lst):
		return 0

	add_on = 0
	if lst[index][0] > cur[0] and lst[index][1] > cur[1]:
		add_on =  1
	return add_on + max(helper(index+1, lst[index], lst), helper(index+1, cur, lst))
	

lst = [(65, 100), (70, 150), (56, 90), (75, 190), (60, 95), (68, 110)]
print(circus_tower(lst))