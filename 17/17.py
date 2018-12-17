from itertools import permutations
from math import sqrt


cities = [
    (7.1, 10.5),
    (18.8, 9.2),
    (2.1, 62.1),
    (74.2, 1.5),
    (58.4, 5.6),
    (15.9, 6.2),
    (44.5, 15.6),
    (88.1, 53.4),
    (36.2, 84.2),
    (26.9, 8.5)
]


def eucledian_distance(a, b):
    # Distances between cities should be cached
    x1, y1 = a
    x2, y2 = b
    return sqrt((x2 - x1) ** 2 +  (y2 - y1) ** 2)


def total_distance(cities):
    total_distance = 0
    for i in range(len(cities) -1):
        total_distance += eucledian_distance(cities[i], cities[i+1])
    return total_distance 


def exhaustive_tsp(cities):
    min_distance = 10e10

    for permutation in permutations(cities):
        min_distance = min(total_distance(permutation), min_distance)
        print(min_distance)

    return min_distance
       

min_distance = exhaustive_tsp(cities)
print(f'{round(min_distance)}')
