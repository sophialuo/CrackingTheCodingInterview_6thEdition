'''
Baby Names: Each year, the govenrment releases a list of the 10,000 most common baby names and their frequencies
(the number of babies with that name). The only problem with this is that some names have multiple spellings.
For example "John" and "Jon" are essentially the same name but would be listed separately in the list. Given
two lists, one of names/frequences and the other of pairs of equivalent names, write an algorithm to print a
 new list of the true frequency of each name. Note that if John and jon are synonyms, and Jon and Johnny are
 synonyms, then Johnand Johnny are synonymes. (It is both transitive an symmetric.) In the final list, any
 name can be used as the "real" name.

 EXAMPLE
 Input:
 	Names: John (15), Jon (12), Chris (13), Kris (4), Christopher (19)
 	Synonyms: (Jon, John), (John, Johnny), (Chris, Kris), (Chris, Christopher)
 Output: John (27), Kris (36)

'''

def baby_names(names, synonyms):
	freqs = {}
	for tupl in names:
		freqs[tupl[0]] = tupl[1]
	
	#create adjacency list
	graph = {}
	for tupl in synonyms:
		key, value = tupl
		if key in graph:
			graph[key].append(value)
		else:
			graph[key] = [value,]
	
	#BFS
	visited = set()
	for node in graph:
		if node not in visited:
			visited.add(node)
			queue = [node]
			total = freqs[node]
			while queue:
				curNode = queue.pop(0)
				if curNode in graph:
					for neighbor in graph[curNode]:
						if neighbor not in visited:
							visited.add(neighbor)
							queue.append(neighbor)
							if neighbor in freqs:
								total += freqs[neighbor]
								freqs.pop(neighbor)
			freqs[node] = total
		elif node in freqs:
			freqs.pop(node)
	
	return freqs
	

names = [("John", 15), ("Jon", 12), ("Chris", 13), ("Kris", 4), ("Christopher", 19)]
synonyms = [("Jon", "John"), ("John", "Johnny"), ("Chris", "Kris"), ("Chris", "Christopher")]
print(baby_names(names, synonyms))