import tsp



def nn_tsp(cities, start = None):
	#Start the tour at the first city;
	#At each step extend the tour by moving from the previous
	#city to its nearest neighbor that has not yet been visited.
	if start is None:
		start = tsp.first(cities)
	tour = [start]
	unvisited = set(cities - {start})
	while unvisited:
		C = nearest_neighbor(tour[-1], unvisited)
		tour.append(C)
		unvisited.remove(C)
	return tour


def nearest_neighbor(A, cities):
	#Find the city that is nearest to city A.
	return min(cities, key = lambda c: tsp.distance(c, A))

def length_ratio(cities):
	#The ratio of the tour lengths for nn_tsp and alltours_tsp algorithms
	return tsp.tour_length(nn_tsp(cities)) / tsp.tour_length(tsp.alltours_tsp(cities))

def main():
	#tsp.plot_tsp(tsp.alltours_tsp, tsp.Cities(9))
	tsp.plot_tsp(nn_tsp, tsp.Cities(1000))
	#print(sorted(length_ratio(tsp.Cities(8, seed = i)) for i in range(11)))

if __name__ == '__main__':
	main()
