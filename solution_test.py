import pytest
from solution import *
from convex_hull import *
from random import uniform

s = Solution()

def solution_test1():
    for k in range(100):
        coords = []
        for i in range(3):
            x = round(uniform(-10, 10), 1)
            y = round(uniform(-10, 10), 1)
            if not([x, y] in coords):
                coords.append([x, y])
        assert s.main(coords) == [[], 0]