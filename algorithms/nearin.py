#!/usr/bin/python
# -*- coding: utf-8 -*-


from typing import List, Tuple
import numpy as np
from copy import deepcopy


def nearin(adj_matrix: List[List[int]], start=1) -> Tuple[List[int], int]:
    vertexes = [vertex for vertex in range(1, len(adj_matrix)+1)]
    vertexes.remove(start)

    visited = [start]
    next_vertex = start
    sum = 0

    while vertexes:
        current_min = np.inf, np.inf
        for current_vertex, current_weight in enumerate(adj_matrix[next_vertex-1], 1):
            if current_vertex in vertexes and current_weight < current_min[1]:
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
    m = [[np.inf, 5, 4, 6, 6],
          [8, np.inf, 5, 3, 4],
          [4, 3, np.inf, 3, 1],
          [8, 2, 5, np.inf, 6],
          [2, 2, 7, 0, np.inf]]

    print(nearin(m))