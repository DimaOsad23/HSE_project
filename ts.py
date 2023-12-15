from solution import *
from random import *
from convex_hull import *
from time import time
import matplotlib.pyplot as plt

s1 = Solution()
t1 = []
t2 = []
ox = []
for i in range(4, 26):
    ox.append(i)
    med_t1 = 0
    med_t2 = 0
    k = 20
    for j in range(k):
        coords = []
        while len(coords) != i:
            x = randint(-100, 101) / 10
            y = randint(-100, 101) / 10
            if not([x, y] in coords):
                coords.append([x, y])
        st1 = time()
        sol1 = s1.main(coords)
        en1 = time()
        st2 = time()
        sol2 = s1.main(convex_hull(coords))
        en2 = time()
        med_t1 += en1 - st1
        med_t2 += en2 - st2
        if sol1[1] != sol2[1] or sorted(sol1[0]) != sorted(sol2[0]):
            print('ERROR')
            print(coords)
            print(sol1)
            print(sol2)
    t1.append(med_t1 / k)
    t2.append(med_t2 / k)
plt.subplot(211)
plt.plot(ox, t1, color = 'r')
plt.plot(ox, t2, color = 'g')
t2 = []
ox = []
for i in range(4, 50):
    ox.append(i)
    med_t2 = 0
    k = 20
    for j in range(k):
        coords = []
        while len(coords) != i:
            x = randint(-100, 101) / 10
            y = randint(-100, 101) / 10
            if not([x, y] in coords):
                coords.append([x, y])
        st2 = time()
        sol2 = s1.main(convex_hull(coords))
        en2 = time()
        med_t2 += en2 - st2
    t2.append(med_t2 / k)
plt.subplot(212)
plt.plot(ox, t2)
plt.show()