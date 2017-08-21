'''
Diving Board: You are building a diving board by placing a bunch of planks of wood end-to-end. There are two types of planks, 
one of length shorter and one of length longer. You must use exactly K planks of wood. Write a method to generate all possible lengths 
for the diving board
'''

def diving_board(shorter, longer, K):
	lengths = set()
	for i in range(K):
		lengths.add(shorter*i + longer*(K-i))
	return lengths

print(diving_board(1, 2, 5))