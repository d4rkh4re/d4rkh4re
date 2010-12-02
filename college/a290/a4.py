"""
a4.py
William C. Morris
<d4rkh4re@gmail.com>
"""

import builtins
import math

class Point(builtins.object):

    def __init__(self, x=0, y=0, point=None):
        """
        Point overrides x and y in providing initial position of Point.
        """
        if point != None:
            self.x = point.x
            self.y = point.y
        else:
            self.x = x
            self.y = y

    def __add__(self, other):
        """
        Returns a new Point whose coordinates are the sum of the
        corresponding coordinates in this and other Points.
        """
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return "[" + str(self.x) + ", " + str(self.y) + "]"

    def distance(self, other):
        """
        Returns distance between this point and other.
        """
        return math.sqrt( (self.x - other.x)**2 + (self.y - other.y)**2 )

    def move(self, dx=0, dy=0):
        """
        Change the x and y coordinates of this point by adding dx and dy,
        respectively.
        """
        self.x += dx
        self.y += dy

class TPoint(Point):
    """
    Point with alpha transparency value.
    """
    def __init__(self, x=0, y=0, alpha=1, point=None):
        """
        Alpha is transparency value between 0 (transparent) and 1 (opaque).
        """
        Point.__init__(self, x, y, point)
        self.alpha = alpha

def distance(point1, point2):
    """
    Returns the distance between two points.
    """
    return point1.distance(point2)

if __name__ == '__main__':
    p = Point(3, 4)
    t = TPoint(point=p, alpha=0.5)

    point_distance = distance(Point(1, 0), Point(0,1))
    print(point_distance)
