from __future__ import division
import matplotlib.pyplot as plt
import random
import time
import itertools
import urllib
import csv

def alltours_tsp(cities):
	#Generate all possible tours of the cities 
	#and choose the shortest tour.
	return shortest_tour(alltours(cities))

def shortest_tour(tours):
	#Choose the tour with the minimum tour length.
	return min(tours, key=tour_length)

def alltours(cities):
	#Return a list of tours, each a permutation of cities,
	#but each one starting with the same city.
	start = first(cities)
	Tour = list
	return [[start] + Tour(rest)
			for rest in itertools.permutations(cities - {start})]

def first(collection):
	#Start iterating over collection, and return the first element.
	return next(iter(collection))


def tour_length(tour):
	#THe total of distances between each pair of consecutive
	#cities in the tour.
	return sum(distance(tour[i], tour[i-1])
				for i in range(len(tour)))

#Cities are represented as Points, which are represented
#as complex numbers.

def X(point):
	#The x coordinate of a point.
	return point.real

def Y(point):
	#The y coordinate of a point
	return point.imag

def distance(A, B):
	#The distance between two points
	return abs(A - B)

def Cities(n, width = 900, height = 600, seed = 42):
	#Make a set of n cities, each with random coordinates
	#within a (width X height) rectangle.
	Point = complex
	City = Point
	random.seed(seed * n)
	return frozenset(City(random.randrange(width), random.randrange(height)) 
					for c in range(n))

def plot_tour(tour):
	#plot the cities as circles and the tour as lines between them.
	start = tour[0]
	plot_lines(list(tour) + [start])
	plot_lines([start], 'rs') #Mark the start city with a red square.

def plot_lines(points, style='bo-'):
	#Plot lines to connect a series of points.
	plt.plot(map(X, points), map(Y, points), style)
	plt.axis('scaled'); plt.axis('off')

def plot_tsp(algorithm, cities):
	#Find the solution and time it takes
	t0 = time.clock()
	tour = algorithm(cities)
	t1 = time.clock()
	assert valid_tour(tour, cities)
	plot_tour(tour); plt.show()
	print("{} city tour with length {:.1f} in {:.3f} secs for {}"
			.format(len(tour), tour_length(tour), t1 - t0, algorithm.__name__))

def valid_tour(tour, cities):
	#Is tour a valid tour for these cities?
	return set(tour) == set(cities) and len(tour) == len(cities)



def main():
	plot_tsp(alltours_tsp, Cities(10))

	"""
	alltours = itertools.permutations
	cities = {1, 2, 3}
	print(list(alltours(cities)))	
	print
	print(list(itertools.permutations({1,2,3})))
	"""


if __name__ == '__main__':
	main()