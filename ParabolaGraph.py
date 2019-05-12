"""
Alexander Urbanyak
CS4720(01)
Created: 01-27-2019
Python 3.6
"""

# graphs y = x^2 using graphics.py
# works with any size window (default 200x200)and
# any scale (default is 50 pixels per 1 coordinate system point)

from graphics import *


def graph_2d_plane(x, y):

    if not isinstance(x, int):
        raise TypeError("Window size must be an integer")
    if not isinstance(y, int):
        raise TypeError("Window size must be an integer")

    # one point in the coordinate system is 50 pixels
    scale = 50

    win = GraphWin("Function Graph", x, y)
    # get center point for x
    if x % 2 == 0:
        px = x // 2 - 1
    else:
        px = x//2
    # get center point for y
    if y % 2 == 0:
        py = y // 2 - 1
    else:
        py = y // 2

    # origin of the system tuple
    origin = (px, py)

    # graph 2d plane
    x_axis = Line(Point(0, origin[1]), Point(x-1, origin[1]))
    x_axis.draw(win)
    y_axis = Line(Point(origin[0], 0), Point(origin[0], y-1))
    y_axis.draw(win)

    Line(Point(origin[0] + scale, origin[1]+4), Point(origin[0] + scale, origin[1]-4)).draw(win)
    Line(Point(origin[0] - scale, origin[1] + 4), Point(origin[0]- scale, origin[1] - 4)).draw(win)
    Text(Point(origin[0] + scale, origin[1] + 14), '1').draw(win)
    Text(Point(origin[0] - scale, origin[1] + 14), '-1').draw(win)
    x, y = quadratic(scale, -1, 1, origin)

    for i in range(len(y)):
        # print("X is " + str(x[i]))
        # print("Y is " + str(y[i]))
        p = Point(x[i], y[i])
        p.draw(win)

    win.getMouse()
    win.close()


# returns a tuple of arrays for x and y coordinates
# for a simple quadratic function y = x^2
# pixels_per_point is the scale of the graph
# interval of the graph [x_begin, x_end]
# origin is the origin of the coordinate system
def quadratic(pixels_per_point, x_begin, x_end, origin):

    if not isinstance(x_begin, int):
        raise TypeError("Interval value must be an integer")
    if not isinstance(x_end, int):
        raise TypeError("Interval value must be an integer")

    x_points = []
    y_points = []

    # size of the window for y dimension
    if origin[1] % 2 == 0:
        y_size = origin[1] * 2
    else:
        y_size = (origin[1] + 1) * 2

    # range begins on the negative interval
    if origin[0]+(pixels_per_point*x_begin) < origin[0]:
        # since quadratic function is symmetrical calculate pixels for
        # positive interval of that length and reverse the array of y pixels
        for i in range(origin[0], origin[0] + abs(pixels_per_point * x_begin)):
            x_points.append(i - abs(pixels_per_point * x_begin))
            y_points.append((y_size - (((i - origin[0]) ** 2 / pixels_per_point) + origin[1]))-2)

        y_points.reverse()
        # calculate pixels for the positive side of the function
        for i in range(origin[0], origin[0]+(pixels_per_point*x_end)+1):
            x_points.append(i)
            y_points.append((y_size - (((i - origin[0])**2 / pixels_per_point) + origin[1]))-2)

    # if range begins with 0 or is positive
    else:
        for i in range(origin[0]+(pixels_per_point*x_begin), origin[0]+(pixels_per_point*x_end)+1):
            x_points.append(i)
            y_points.append((y_size - (((i - origin[0]) ** 2 / pixels_per_point) + origin[1]))-2)

    print(y_size)
    return x_points, y_points


if __name__ == '__main__':
    graph_2d_plane(200, 200)
