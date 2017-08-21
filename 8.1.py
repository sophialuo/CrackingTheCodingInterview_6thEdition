'''
Triple Step: A child is runnning up a staircase with n steps ad can hop either 1 step, 2 steps, or 3 steps at a time.
Implement a method to count how many possible ways the child can run up the stairs
'''

def triple_step(n):
	return triple_step_helper(n)

def triple_step_helper(cur):
	if cur == 0:
		return 1
	if cur < 0:
		return 0
	
	return triple_step_helper(cur-1) + triple_step_helper(cur-2) + triple_step_helper(cur-3)
