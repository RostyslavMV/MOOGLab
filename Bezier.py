import numpy as np


# find the a & b points
def get_bezier_coefficients(points):
    # since the formulas work given that we have n+1 points
    # then n must be this:
    n = len(points) - 1

    # build coefficients matrix
    c = 4 * np.identity(n)
    np.fill_diagonal(c[1:], 1)
    np.fill_diagonal(c[:, 1:], 1)
    c[0, n - 1] = 1
    c[n - 1, 0] = 1
    print(c)
    # build points vector
    p = [2 * (2 * points[i] + points[i + 1]) for i in range(n)]
    # solve system, find a & b
    a = np.linalg.solve(c, p)
    b = [0] * n
    for i in range(n):
        b[i] = 2 * points[(i + 1) % n] - a[(i + 1) % n]

    return a, b


# returns the general Bezier cubic formula given 4 control points
def get_cubic(a, b, c, d):
    return lambda t: np.power(1 - t, 3) * a + 3 * np.power(1 - t, 2) * t * b + 3 * (1 - t) * np.power(t,
                                                                                                      2) * c + np.power(
        t, 3) * d


# return one cubic curve for each consecutive points
def get_bezier_cubic(points):
    a, b = get_bezier_coefficients(points)
    return [
        get_cubic(points[i], a[i], b[i], points[i + 1])
        for i in range(len(points) - 1)
    ]


# evaluate each cubic curve on the range [0, 1] sliced in n points
def evaluate_bezier(points, n):
    curves = get_bezier_cubic(points)
    return np.array([fun(t) for fun in curves for t in np.linspace(0, 1, n)])


# fit the points with Bezier interpolation
# use 50 points between each consecutive points to draw the curve

def get_bezier_curve_for_hull(quick_hull):
    quick_hull.append(quick_hull[0])
    return evaluate_bezier(np.array(quick_hull), 50)
