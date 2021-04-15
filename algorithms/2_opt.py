#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List, Dict, Tuple
import numpy as np


def k_opt_2(adj_matrix: List[List[int]], start=1) -> Tuple[List[int], int]:
    has_distance_changed = True


    while has_distance_changed:
        


