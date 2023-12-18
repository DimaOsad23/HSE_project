# Алгоритм нахождения выпуклой взят из книжки
# "Алгоритмы. Введение в разработку и анализ", Ананий Левитин


def convex_hull(coords):
    '''
    Find convex hull of a set of points

    :param coords: the list with coordinates of points
    :type coords: list
    :returns: convex hull of a set of points
    :rtype: list
    :note: if length of convex hull is three return list with all points
    '''
    coords.sort()
    p1 = 0
    p2 = len(coords) - 1
    hull_2 = []
    if p2 > 0:
        hull_1 = sorted(
            upper_hull(
                coords,
                p1,
                p2) +
            upper_hull(
                coords,
                p2,
                p1))
        hull_2.append(hull_1[0])
        for i in range(1, len(hull_1)):
            if hull_1[i] != hull_1[i - 1]:
                hull_2.append(hull_1[i])
        if len(hull_2) < 4:
            return coords
    return hull_2


#
def upper_hull(coords, p1, p2):
    '''
    Find upper convex hull of a set of points

    :param coords: the list with coordinates of points
    :type coords: list
    :param p1: index of the first point of upper convex hull
    :type p1: int
    :param p2: index of the last point of upper convex hull
    :returns: upper convex hull of a set of points without first point
    :rtype: list
    '''
    sp = None
    step = (p2 - p1) // abs(p2 - p1)
    for p3 in range(p1 + 1 * step, p2, step):
        d = (
            int(100 * coords[p1][0] * coords[p2][1])
            + int(100 * coords[p3][0] * coords[p1][1])
            + int(100 * coords[p2][0] * coords[p3][1])
            - int(100 * coords[p3][0] * coords[p2][1])
            - int(100 * coords[p2][0] * coords[p1][1])
            - int(100 * coords[p1][0] * coords[p3][1])
        )
        if (sp is None or d > sp) and d >= 0:
            sp = d
            p_m = p3
    if sp is None:
        return [coords[p2]]
    return upper_hull(coords, p1, p_m) + upper_hull(coords, p_m, p2)


######
