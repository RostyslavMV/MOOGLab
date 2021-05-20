def calc_distance(left_point, right_point, point) -> float:
    x1 = left_point[0]
    y1 = left_point[1]
    x2 = right_point[0]
    y2 = right_point[1]
    x0 = point[0]
    y0 = point[1]
    return (y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1


def farthest_point(points, left_point, right_point):
    dist = -1
    answer = [0, 0]
    for point in points:
        new_dist = abs(calc_distance(left_point, right_point, point))
        if new_dist > dist:
            dist = new_dist
            answer = point
    return answer


def points_on_the_left(points, left_point, right_point):
    answer = []
    for point in points:
        if calc_distance(left_point, right_point, point) <= 0:
            answer.append(point)
    return answer


def quick_convex_hull(points, left_point, right_point):
    if len(points) == 0:
        return []
    if points == [left_point, right_point]:
        return [left_point, right_point]
    elif points == [right_point, left_point]:
        return [left_point, right_point]
    elif points == [left_point]:
        return [left_point]
    elif points == [right_point]:
        return [right_point]
    else:
        h = farthest_point(points, left_point, right_point)
        if h == left_point or h == right_point:
            return [left_point, right_point]
        points1 = points_on_the_left(points, left_point, h)
        points2 = points_on_the_left(points, h, right_point)
        return quick_convex_hull(points1, left_point, h) + quick_convex_hull(points2, h, right_point)


def get_hull_for_points_from_file():
    points = read_points()
    fp = first_point(points)
    hull = quick_convex_hull(points, fp, fp)

    res_hull = []
    for i in hull:
        if i not in res_hull:
            res_hull.append(i)

    return points, res_hull


def read_points():
    fv = open("points.txt")
    points = []
    for line in fv.readlines():
        coordinates = [float(i) for i in line.split(" ")]
        points.append([coordinates[0], coordinates[1]])
    fv.close()

    return points


def first_point(points):
    res = points[0]
    for point in points:
        if point[0] < res[0]:
            res = point
    return res
