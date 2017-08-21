'''
Parens: Implement an algorithm to print all valid (i.e. properly opened and closed) combinatoins of n pairs of parentheses

EXAMPLE
Input:3
Output: ((())), ((),()), (())(), ()(()), ()()()
'''

def parens(num):
	parens_helper('(', 1, 0, num)

def parens_helper(cur_combo, left, right, num):
	lst = []
	if left == num and right == num:
		print(cur_combo)
	elif left == num:
		parens_helper(cur_combo + ')', left, right+1, num)
	elif left == right:
		parens_helper(cur_combo + '(', left+1, right, num)
	elif left > right:
		parens_helper(cur_combo + '(', left+1, right, num)
		parens_helper(cur_combo + ')', left, right+1, num)

parens(5)