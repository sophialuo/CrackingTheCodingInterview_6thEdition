'''16.10
Living People: Given a list of people with their birth and death years, implement a method to compute the year with the most number of people alive.
You may assume that all people were born between 1900 and 2000 (inclusive). If a person was alive during any portion of that year, they should be 
included in that year's count. For example, Person (birth = 1908, death = 1909) is included in the counts for both 1908 and 1909.
'''
#lst of tuples is input
def living_people(lst):
	births, deaths = {}, {}
	min_birth, max_death = 99999999999, -1
	for tupl in lst:
		birth, death = tupl
		death = death+1
		
		if birth in births:
			births[birth] += 1
		else:
			births[birth] = 1

		if death in deaths:
			deaths[death] += 1
		else:
			deaths[death] = 1

		if birth < min_birth:
			min_birth = birth
		if death > max_death:
			max_death = death

	max_alive = -1
	max_year = 0
	cur_alive = 0

	for year in range(min_birth, max_death + 1):
		if year in births:
			cur_alive += births[year]
		if year in deaths:
			cur_alive -= deaths[year]

		if cur_alive > max_alive:
			max_year, max_alive = year, cur_alive

	return(max_year, max_alive)

lst = [(1, 2), (2, 5), (1, 4), (3, 6), (4, 8), (5, 7), (8, 10), (9, 10), (6, 6)]
print(living_people(lst))