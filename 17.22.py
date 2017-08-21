'''
17.22 
Word Transformer: Given two owrds of equal length that are in a dictionary, write a method to transform one word into another word by 
changing only one letter at a time. The new word you get in ech step must be in the dictionary.
'''


def is_one_letter_away(word, compare):

	counter = 0
	for i in range(len(word)):
		if word[i] != compare[i]:
			counter += 1
		if counter > 1:
			return False
	if len(word) != len(compare):
		counter += 1

	return True


def word_transformer(dictionary, start_word, target_word):
	dictionary = list(dictionary)
	adj_list = {}
	start_vertex = None
	for i in range(len(dictionary)):
		word = dictionary[i]
		for j in range(i+1, len(dictionary)):
			compare = dictionary[j]
			if is_one_letter_away(word, compare):
				if word in adj_list:
					adj_list[word].append(compare)
				else:
					adj_list[word] = [compare]

				if compare in adj_list and word not in adj_list[compare]:
					adj_list[compare].append(word)
				else:
					adj_list[compare] = [word]

		if start_vertex is None and is_one_letter_away(start_word, word):
			start_vertex = word

	if start_vertex == None:
		return None

	queue = [(start_vertex, [start_vertex])]
	while queue:
		vertex, path = queue.pop(0)
		if vertex == target_word:
			return [start_word]+path+[target_word]

		for neighbor in adj_list[vertex]:
			if neighbor not in path:
				queue.append((neighbor, path+[neighbor]))

	return None

	

dictionary = {'POON', 'PLEE', 'SAME', 'POIE', 'PLEA', 'PLIE', 'POIN'}
start = 'TOON'
target = 'PLEA'
print(word_transformer(dictionary, start, target))