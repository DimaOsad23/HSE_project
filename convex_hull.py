#####Алгоритм нахождения выпуклой взят из книжки  "Алгоритмы. Введение в разработку и анализ", Ананий Левитин
def convex_hull(coords):
    coords.sort()
    p1 = 0
    p2 = len(coords) - 1
    hull_1 = upper_hull(coords, p1, p2) + upper_hull(coords, p2, p1)
    hull_1.sort()
    hull_2 = [hull_1[0]]
    for i in range(1, len(hull_1)):
        if hull_1[i] != hull_1[i - 1]:
            hull_2.append(hull_1[i])
    print(hull_2)
    if len(hull_2) < 4:
        return coords
    return hull_2

def upper_hull(coords, p1, p2):
    sp = None
    step = (p2 - p1) // abs(p2-p1)
    for p3 in range(p1 + 1*step, p2, step):
        d = (int(100*coords[p1][0]*coords[p2][1]) + int(100*coords[p3][0]*coords[p1][1]) + int(100*coords[p2][0]*coords[p3][1]) -
             int(100*coords[p3][0]*coords[p2][1]) - int(100*coords[p2][0]*coords[p1][1]) - int(100*coords[p1][0]*coords[p3][1]))
        if (sp == None or d > sp) and d >= 0:
            sp = d
            p_m = p3
    if sp == None:
        return [coords[p2]]
    return (upper_hull(coords, p1, p_m) + upper_hull(coords, p_m, p2))
######

