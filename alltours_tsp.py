import tsp


def alltours_tsp(cities):
	#Generate all possible tours of the cities 
	#and choose the shortest tour.
	return shortest_tour(alltours(cities))

def alltours(cities):
	#Return a list of tours, each a permutation of cities,
	#but each one starting with the same city.
	start = first(cities)
	Tour = list
	return [[start] + Tour(rest)
			for rest in itertools.permutations(cities - {start})]



