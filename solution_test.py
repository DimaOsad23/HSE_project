import pytest
from solution import *
from convex_hull import *
from random import *



def test1():
    s = Solution()
    for k in range(1000):
        coords = []
        for i in range(3):
            x = round(uniform(-10, 10), 1)
            y = round(uniform(-10, 10), 1)
            if not([x, y] in coords):
                coords.append([x, y])
        assert s.main(coords) == ([], 0)

def test2():
    s = Solution()
    for k in range(1000):
        coords = []
        for i in range(3):
            x = round(uniform(-10, 10), 1)
            y = round(uniform(-10, 10), 1)
            if not([x, y] in coords):
                coords.append([x, y])
        assert s.main(convex_hull(coords)) == ([], 0)

def test3():
    s = Solution()
    for i in range(4, 10):
        coords = []
        for j in range(i + 1):
            coords.append([j, j])
        assert s.main(coords) == ([], 0)

def test4():
    s = Solution()
    for i in range(4, 10):
        coords = []
        for j in range(i + 1):
            coords.append([j, j])
        assert s.main(convex_hull(coords)) == ([], 0)

def test5():
    s = Solution()
    for i in range(4, 10):
        coords = []
        for j in range(i + 1):
            coords.append([j, j])
        coords.append([j, j+ 5])
        assert s.main(coords) == ([], 0)

def test6():
    s = Solution()
    for i in range(4, 10):
        coords = []
        for j in range(i + 1):
            coords.append([j, j])
        coords.append([j, j + 5])
        assert s.main(convex_hull(coords)) == ([], 0)

def test7():
    s = Solution()
    coords = [[-6.0, 6.8], [-5.8, 3.0], [-3.3, -3.5],
              [-3.1, 3.1], [-3.0, 4.4], [-2.5, 0.6],
              [-1.8, -0.9], [-1.3, 7.1], [2.1, 3.4],
              [2.1, 7.2], [3.1, 0.8], [5.4, -2.2], [6.4, 4.2]]
    res = s.main(coords)
    assert round(res[1], 3) == 87.54 and sorted(res[0]) == [[-6, 6.8], [-3.3, -3.5], [5.4, -2.2], [6.4, 4.2]]

def test8():
    s = Solution()
    coords = [[-6.0, 6.8], [-5.8, 3.0], [-3.3, -3.5],
              [-3.1, 3.1], [-3.0, 4.4], [-2.5, 0.6],
              [-1.8, -0.9], [-1.3, 7.1], [2.1, 3.4],
              [2.1, 7.2], [3.1, 0.8], [5.4, -2.2], [6.4, 4.2]]
    res = s.main(convex_hull(coords))
    assert round(res[1], 3) == 87.54 and sorted(res[0]) == [[-6, 6.8], [-3.3, -3.5], [5.4, -2.2], [6.4, 4.2]]

def test9():
    s = Solution()
    for i in range(16):
        k = 20
        for j in range(k):
            coords = []
            while len(coords) != i:
                x = randint(-100, 101) / 10
                y = randint(-100, 101) / 10
                if not ([x, y] in coords):
                    coords.append([x, y])
            sol1 = s.main(coords)
            sol2 = s.main(convex_hull(coords))
            assert sol1[1] == sol2[1] and sorted(sol1[0]) == sorted(sol2[0])

def test_f_q_1():
    s = Solution()
    assert s.false_quadrilateral([-7.0, 5.0], [-6.0, 6.0], [-5.0, 7.0], [-3.5, 3.5]) == 1

def test_f_q_2():
    s = Solution()
    assert s.false_quadrilateral([-7.0, 5.0], [-6.1, 6.0], [-5.0, 7.0], [-3.5, 3.5]) == 0

def test_f_q_3():
    s = Solution()
    assert s.false_quadrilateral([-7.5, 7.4], [-2.6, 7.6], [-4.4, 2.4], [-4.8, 5.2]) == 0

def test_f_q_4():
    s = Solution()
    assert s.false_quadrilateral([1, 1], [2, 2], [3, 3], [4, 4]) == 1