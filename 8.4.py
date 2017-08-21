'''
Power Set: Write a method to return all subsets of a set
'''

def power_set(lst):
	if lst == []:
		return [[]]
	sub = power_set(lst[1:])

	return sub + [[lst[0]] + num for num in sub]

print(power_set([]))
print(power_set([1]))
print(power_set([1, 2, 3, 4, 5]))