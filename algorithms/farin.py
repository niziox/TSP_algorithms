#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List, Tuple
import numpy as np
from copy import deepcopy


def farin(adj_matrix: List[List[int]], start=1) -> Tuple[List[int], int]:
    vertexes = [vertex for vertex in range(1, len(adj_matrix)+1)]
    vertexes.remove(start)

    visited = [start]
    next_vertex = start
    sum = 0

    while vertexes:
        current_min = np.inf, -1
        for current_vertex, current_weight in enumerate(adj_matrix[next_vertex-1], 1):
            if current_vertex in vertexes and current_weight > current_min[1]:
                current_min = current_vertex, current_weight

        min_combination = np.inf, np.inf
        for current_place in range(len(visited)):
            visited = visited[:current_place+1] + [current_min[0]] + visited[current_place+1:]
            sum_combination_current = 0

            for current_visited in range(len(visited) - 1):
                sum_combination_current += adj_matrix[visited[current_visited]-1][visited[current_visited+1]-1]
            sum_combination_current += adj_matrix[visited[-1]-1][visited[0]-1]

            if sum_combination_current < min_combination[1]:
                min_combination = deepcopy(visited), sum_combination_current

            visited.remove(current_min[0])

        next_vertex = current_min[0]
        visited = min_combination[0]
        vertexes.remove(next_vertex)
        sum = min_combination[1]

    visited.append(start)

    return visited, sum


if __name__ == '__main__':
    # m1 = [[np.inf, 5, 4, 6, 6],
    #       [8, np.inf, 5, 3, 4],
    #       [4, 3, np.inf, 3, 1],
    #       [8, 2, 5, np.inf, 6],
    #       [2, 2, 7, 0, np.inf]]
    #
    # for i in range(1, len(m1)+1):
    #     print(farin(m1, i), end='\n\n')

    # m2 = [[np.inf, 5, 4, 6, 6, 5],
    #       [8, np.inf, 5, 3, 4, 3],
    #       [4, 3, np.inf, 3, 1, 1],
    #       [8, 2, 5, np.inf, 6, 7],
    #       [2, 2, 7, 0, np.inf, 9],
    #       [5, 7, 8, 3, 0, 1, np.inf]]
    #
    # for i in range(1, len(m2)+1):
    #     print(farin(m2, i), end='\n\n')

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
        print(farin(m3, i), end='\n\n')

