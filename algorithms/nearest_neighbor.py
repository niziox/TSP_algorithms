#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List, Tuple
import numpy as np


def nearest_neighbor(adj_matrix: List[List[int]], start=1) -> Tuple[List[int], int]:
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
        next_vertex = current_min[0]
        visited.append(next_vertex)
        sum += current_min[1]
        vertexes.remove(next_vertex)

    visited.append(start)
    sum += adj_matrix[next_vertex-1][start-1]

    return visited, sum


if __name__ == '__main__':
    m = [[np.inf, 5, 4, 6, 6],
          [8, np.inf, 5, 3, 4],
          [4, 3, np.inf, 3, 1],
          [8, 2, 5, np.inf, 6],
          [2, 2, 7, 0, np.inf]]

    print(nearest_neighbor(m, 5))
