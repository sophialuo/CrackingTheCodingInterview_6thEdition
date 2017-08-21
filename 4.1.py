'''
Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
'''

def route_exists(graph, start, end):
	queue = [start]
	visited = set()
	visited.add(start)
	while queue:
		vertex = queue.pop()
		if vertex == end:
			return True
		if vertex in graph:
			for adj in graph[vertex]:
				if adj not in visited:
					visited.add(adj)
					queue.append(adj)	
	return False


graph1 = {'A': ['B'], 'B': ['C'], 'C': ['D'], 'D':['B','E']}
graph2 = {'A': ['B', 'C', 'D'], 'C': ['D','E'], 'D': ['E']}
graph3 = {'A': ['B','C'], 'C': ['D','E']}
count = 0

if route_exists(graph1, 'A', 'E') and not route_exists(graph1, 'D', 'A'):
	print('correct')
	count += 1
else:
	print('incorrect, check graph1')
if route_exists(graph2, 'A', 'E') and not route_exists(graph2, 'D', 'C'):
	print('correct')
	count += 1
else:
	print('incorrect, check graph2')
if route_exists(graph3, 'A', 'E') and not route_exists(graph3, 'D', 'B'):
	print('correct')
	count += 1
else:
	print('incorrect, check graph3')

if count == 3:
	print('all correct!')