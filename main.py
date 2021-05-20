import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patches

from Bezier import get_bezier_curve_for_hull
from QuickHull import get_hull_for_points_from_file


def draw(points, bezier_curve, all_points):
    fig, ax = plt.subplots()
    plt.xticks([i1 for i1 in range(-20, 20)]), plt.yticks([i1 for i1 in range(-20, 20)])
    plt.plot(points[:, 0], points[:, 1], 'ro:')
    for point in all_points:
        circle = patches.Circle((point[0], point[1]), radius=0.15, color='r')
        ax.add_patch(circle)
    plt.plot(bezier_curve[:, 0], bezier_curve[:, 1], 'b')


points_from_file, hull = get_hull_for_points_from_file()
curve = get_bezier_curve_for_hull(hull)
hull.append(hull[0])
draw(np.array(hull), curve, points_from_file)
plt.show()
