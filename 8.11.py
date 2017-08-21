'''
Coins: Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and pennies (1 cent), write coe to calculate
the number of ways of representing n cents
'''

def coins(amount):
	return coins_helper(amount)

def coins_helper(amount):
	if amount < 0:
		return 0
	elif amount == 0:
		return 1
	else:
		return coins_helper(amount-25) + coins_helper(amount-10) + coins_helper(amount-5) + coins_helper(amount-1)

print(coins(1))
print(coins(5))
print(coins(7))

#note: 5, 1, 1 is different from 1, 5, 1