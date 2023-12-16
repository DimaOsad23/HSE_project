import pytest
from convex_hull import *

def test_convex_hull_1():
    coords = [[-5.8, 7.2], [-5.5, -4.5], [-3.7, -1.3], [-3.5, 3.0], [-2.7, 1.4], [-2.2, 4.3], [-1.7, 2.6], [-1.6, 1.9], [1.6, 4.3], [5.1, 5.9]]
    assert convex_hull(coords) == sorted(coords)

def test_convex_hull_2():
    coords = [[1.0, 1.0], [2.0, 2.0], [3.0, 3.0], [4.0, 4.0]]
    assert convex_hull(coords) == sorted(coords)

def test_convex_hull_3():
    coords = [[-7.8, 5.5], [-4.5, 6.8]]
    assert convex_hull(coords) == sorted(coords)

def test_convex_hull_4():
    coords = [[-10.0, 1.2], [-9.5, -5.7], [-9.4, 6.7],
              [-9.1, -9.8], [-8.2, 1.7], [-7.8, 0.4],
              [-6.2, 5.2], [-6.1, -3.6], [-4.6, 8.0],
              [-3.5, 4.9], [-3.4, 3.4], [-2.1, -1.3],
              [-0.1, -6.7], [0.1, -3.1], [2.0, 5.6],
              [3.8, -2.2], [3.9, 5.0], [3.9, 8.1],
              [4.8, -5.3], [4.8, -0.9], [4.9, -4.9],
              [5.1, -7.3], [5.9, 6.5], [6.2, 5.2], [6.8, -3.8]]
    assert convex_hull(coords) == [[-10.0, 1.2], [-9.5, -5.7], [-9.4, 6.7],
                                   [-9.1, -9.8], [-4.6, 8.0], [3.9, 8.1],
                                   [5.1, -7.3], [5.9, 6.5], [6.2, 5.2], [6.8, -3.8]]

def test_convex_hull_5():
    coords = [[-6.8, 5.5], [-5.3, 8.6], [4.1, 7.8]]
    assert convex_hull(coords) == coords

def test_convex_hull_6():
    coords = [[-8.0, 4.0], [-8.0, 5.0], [-8.0, 5.9], [-8.0, 8.0], [-6.2, 2.5], [-4.7, 7.7], [-4.1, 2.7], [-2.9, 5.6]]
    assert convex_hull(coords) == coords

def test_convex_hull_7():
    coords = [[-8.0, 4.0], [-8.0, 5.0], [-8.0, 5.9], [-8.0, 8.0], [-6.2, 2.5], [-5.0, 5.0], [-4.1, 2.7], [-2.9, 5.6]]
    assert convex_hull(coords) == [[-8.0, 4.0], [-8.0, 5.0], [-8.0, 5.9], [-8.0, 8.0], [-6.2, 2.5], [-4.1, 2.7], [-2.9, 5.6]]

def test_convex_hull_8():
    coords = [[-7.9, 3.1], [-7.9, 3.6], [-7.9, 4.4],
              [-6.0, 6.0], [-5.6, 6.0], [-5.2, 6.0],
              [-4.6, 6.0], [-2.0, 4.0], [-4.9, 1.0],
              [-5.6, 2.9], [-5.6, 4.1], [-5.0, 3.8],
              [-5.0, 2.8], [-3.7, 4.3]]
    assert sorted(convex_hull(coords)) == [[-7.9, 3.1], [-7.9, 3.6], [-7.9, 4.4],
                                           [-6.0, 6.0], [-5.6, 6.0], [-5.2, 6.0],
                                           [-4.9, 1.0], [-4.6, 6.0], [-2.0, 4.0]]

def test_convex_hull_9():
    for i in range(10):
        coords = [[i, i]]
        assert convex_hull(coords) == []

def test_convex_hull_10():
    coords = []
    assert convex_hull(coords) == []

def test_upper_hull_1():
    coords = [[-6.0, 6.0], [-4.9, 6.0], [-4.0, 6.0]]
    assert sorted(upper_hull(coords, 0, 2)) == [[-4.9, 6.0], [-4.0, 6.0]]

def test_upper_hull_2():
    coords = [[-6.0, 5.0], [-5.1, 5.0], [-3.9, 5.0], [-3.3, 5.0]]
    assert sorted(upper_hull(coords, 0, 3)) == [[-5.1, 5.0], [-3.9, 5.0], [-3.3, 5.0]]

def test_upper_hull_3():
    coords = [[-6.0, 5.0], [-5.1, 5.0], [-3.9, 5.0], [-3.3, 5.0]]
    assert sorted(upper_hull(coords, 0, 2)) == [[-5.1, 5.0], [-3.9, 5.0]]

def test_upper_hull_4():
    coords = [[-7.6, 6.2], [-4.4, 6.2], [-3.3, 4.9], [-1.3, 6.3]]
    assert sorted(upper_hull(coords, 0, 3)) == [[-1.3, 6.3]]

def test_upper_hull_5():
    coords = [[-6.0, 6.0], [-4.9, 6.0], [-4.0, 6.0]]
    assert sorted(upper_hull(coords, 2, 0)) == [[-6.0, 6.0], [-4.9, 6.0]]

def test_upper_hull_6():
    coords = [[-6.0, 5.0], [-5.1, 5.0], [-3.9, 5.0], [-3.3, 5.0]]
    assert sorted(upper_hull(coords, 3, 0)) == [[-6.0, 5.0], [-5.1, 5.0], [-3.9, 5.0]]

def test_upper_hull_7():
    coords = [[-6.0, 5.0], [-5.1, 5.0], [-3.9, 5.0], [-3.3, 5.0]]
    assert sorted(upper_hull(coords, 2, 0)) == [[-6.0, 5.0], [-5.1, 5.0]]

def test_upper_hull_8():
    coords = [[-7.6, 6.2], [-4.4, 6.2], [-3.3, 4.9], [-1.3, 6.3]]
    assert sorted(upper_hull(coords, 3, 0)) == [[-7.6, 6.2], [-3.3, 4.9]]

def test_upper_hull_9():
    coords = [[1, 1], [2, 2]]
    assert sorted(upper_hull(coords, 0, 1)) == [[2, 2]]

def test_upper_hull_10():
    coords = [[1, 1], [2, 2]]
    assert sorted(upper_hull(coords, 1, 0)) == [[1, 1]]

