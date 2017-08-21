'''
Group Anagrams: Write a method to sort an array of strings so that all the anagrams are next to each other
'''


def group_anagrams(lst):
	perms = {}
	for string in lst:
		perm = derive_perm(string)
		if perm in perms:
			perms[perm].append(string)
		else:
			perms[perm] = [string]
	
	grouped_lst = []
	for perm in perms:
		grouped_lst += perms[perm]
	
	return grouped_lst

def derive_perm(string):
	counts = {}
	for char in string:
		if char in counts:
			counts[char] += 1
		else:
			counts[char] = 1
	
	perm = []
	for letter in counts:
		perm.append((letter, counts[letter]))
	perm = tuple(sorted(perm))

	return perm

test = ['abc', 'defg', 'cba', 'xy', 'efdg', 'bac', 'yx', 'z']
print(group_anagrams(test))