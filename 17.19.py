'''
17.19 
Missing Two: You are given an array with all the numbers from 1 to N appearing exactly once, except for one number that is 
missing. How can you find the missing number in O(N) time and O(1) space? What if there were two numbers missing?
'''
def missing_one(lst, N):
	total = sum(lst)
	actual = sum(range(1, N+1))
	diff = actual-total
	if diff == 0:
		return None
	return diff

def missing_two(lst, N):
	total = sum(lst)
	actual = sum(range(1, N+1))
	diff = actual-total
	for i in range(1, diff+1):
		if i not in lst and diff-i not in lst:
			return (i, diff-i)
	return None

lst = [1, 2, 3, 4, 6, 7, 8, 9, 10] #missing five
print(missing_one(lst, 10))
lst = [1, 2, 4, 6, 7, 8, 9, 10] #missing five and three
print(missing_two(lst, 10))