'''
17.15 
Longest Word: Given a list of words, write a program to find the longest word made of other words in a list.

EXAMPLE
Input: cat, banana, dog, nana, walk, walker, dogwalker
Output: dogwalker
'''
class Node(object):
	def __init__(self, value, children = []):
		self.value = value
		self.children = []

def add_to_node(node, word):
	children = node.children
	cur_node = node
	stripPrefix = ""
	while children:
		flag = False
		for child in children:
			prefix = child.value
			if word.index(prefix) == 0:
				stripPrefix = word[len(prefix):]
				children = child.children
				cur_node = child
				flag = True

		if not flag:
			cur_node.children.append(Node(value = word))
			break

def longest_word(lst):
	lst.sort(key = lambda s: len(s))
	lst = list(set(lst)) #get rid of duplicates

	cur_max = ''
	tree = []
	for word in lst:
		flag= False
		for node in tree: 
			prefix = node.value
			if prefix in word and word.index(prefix) == 0:
				stripPrefix = word[len(prefix):]
				add_to_node(node, stripPrefix)
				flag = True

				if len(word) > len(cur_max):
					cur_max = word

		if not flag: #new prefix
			tree.append(Node(value = word))

	return cur_max #is empty string if such a word does not exist



lst = ['cat', 'banana', 'catdog', 'dog', 'nana', 'do', 'dobananawalker', 'walk', 'walker', 'dogwalker']
print(longest_word(lst))
