#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List, Tuple
import numpy as np
from nearin import nearin
from farin import farin
from nearest_neighbor import nearest_neighbor


def calculate_total_distance(existing_route: List[int], adj_matrix: List[List[int]]) -> int:
    total_distance = 0
    for current_vertex in range(len(existing_route) - 1):
        total_distance += adj_matrix[existing_route[current_vertex]-1][existing_route[current_vertex+1]-1]

    return total_distance


def opt_2(adj_matrix: List[List[int]], start=1, genetic_algorithm: str = 'increasing') -> Tuple[List[int], int]:
    has_distance_changed = True

    if genetic_algorithm == 'increasing':
        existing_route = [start] + [vertex for vertex in range(1, len(adj_matrix) + 1) if vertex != start] + [start]
        best_distance = calculate_total_distance(existing_route, adj_matrix)
    elif genetic_algorithm == 'nearest_neighbor':
        existing_route, best_distance = nearest_neighbor(adj_matrix, start)
    elif genetic_algorithm == 'farin':
        existing_route, best_distance = farin(adj_matrix, start)
    elif genetic_algorithm == 'nearin':
        existing_route, best_distance = nearin(adj_matrix, start)
    else:
        raise ValueError('Wrong argument, choose from: increasing, nearest_neighbor, farin, nearin')

    while has_distance_changed:
        has_distance_changed = False

        for i in range(1, len(existing_route)-2):
            for k in range(i+2, len(existing_route)):
                new_route = existing_route[:i] + existing_route[i:k][::-1] + existing_route[k:]
                new_distance = calculate_total_distance(new_route, adj_matrix)
                if new_distance < best_distance:
                    existing_route = new_route
                    best_distance = new_distance
                    has_distance_changed = True

    return existing_route, best_distance


if __name__ == '__main__':
    # m1 = [[np.inf, 5, 4, 6, 6],
    #       [8, np.inf, 5, 3, 4],
    #       [4, 3, np.inf, 3, 1],
    #       [8, 2, 5, np.inf, 6],
    #       [2, 2, 7, 0, np.inf]]
    #
    # for i in range(1, len(m1)+1):
    #     print(opt_2(m1, i), end='\n\n')

    # m2 = [[np.inf, 5, 4, 6, 6, 5],
    #       [8, np.inf, 5, 3, 4, 3],
    #       [4, 3, np.inf, 3, 1, 1],
    #       [8, 2, 5, np.inf, 6, 7],
    #       [2, 2, 7, 0, np.inf, 9],
    #       [5, 7, 8, 3, 0, 1, np.inf]]
    #
    # for i in range(1, len(m2)+1):
    #     print(opt_2(m2, i), end='\n\n')

    m3 = [[np.inf, 5, 4, 6, 6, 5, 2, 7, 3, 9],
          [8, np.inf, 5, 3, 4, 3, 8, 10, 5, 3],
          [4, 3, np.inf, 3, 1, 1, 0, 8, 4, 5],
          [8, 2, 5, np.inf, 6, 7, 10, 5, 1, 13],
          [2, 2, 7, 0, np.inf, 9, 3, 6, 1, 11],
          [5, 7, 8, 3, 1, np.inf, 6, 1, 8, 0],
          [3, 6, 8, 14, 0, 3, np.inf, 12, 4, 7],
          [16, 6, 3, 1, 9, 4, 2, np.inf, 8, 5],
          [4, 7, 2, 1, 8, 5, 4, 4, np.inf, 3],
          [1, 9, 2, 8, 3, 7, 4, 6, 4, np.inf]]

    for i in range(1, len(m3)+1):
        try:
            print(opt_2(m3, i, 'nearin'), end='\n\n')
        except ValueError as error_msg:
            print(error_msg)
