import tsp
import nn_tsp

def repeated_nn_tsp(cities):
	#Repeat the nn_tsp algorithm starting from each city;
	#Return the shortest tour.
	return tsp.shortest_tour(nn_tsp.nn_tsp(cities, start)
								for start in cities)


def main():
	tsp.plot_tsp(nn_tsp.nn_tsp, tsp.Cities(9))
	tsp.plot_tsp(repeated_nn_tsp, tsp.Cities(9))
	tsp.plot_tsp(tsp.alltours_tsp, tsp.Cities(9))

if __name__ == '__main__':
	main()