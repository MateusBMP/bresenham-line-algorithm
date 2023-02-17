import matplotlib.pyplot as plt
import os
import sys
from typing import NamedTuple, List

class Coordinates(NamedTuple):
    x: int
    y: int

def inc_line(start: Coordinates, end: Coordinates) -> List[Coordinates]:
    points: List[Coordinates] = []
    dx = end.x - start.x
    dy = end.y - start.y
    d = 2 * dy - dx
    incrE = 2 * dy
    incrNE = 2 * (dy - dx)
    x = start.x
    y = start.y

    points.append(Coordinates(x, y))
    while x < end.x:
        if d <= 0:
            d += incrE
            x += 1
        else:
            d += incrNE
            x += 1
            y += 1
        points.append(Coordinates(x, y))

    return points

def main(start: Coordinates, end: Coordinates) -> bool:
    points = inc_line(start, end)

    # Print coordinates
    for i, point in enumerate(points):
        print("c{}({},{})".format(i + 1, point.x, point.y))

    # Plot coordinates
    data = []
    for i in range(0, max(start.x, end.x) + 2):
        line = []
        for j in range(0, max(start.y, end.y) + 2):
            if Coordinates(i, j) in points:
                line.append(1)
            else:
                line.append(0)
        data.append(line)
    plt.imshow(data, cmap="gray", interpolation="nearest")
    plt.savefig(os.path.join(os.path.dirname(__file__), "output", "output.png"))

    print("output saved to {}".format(os.path.join(os.path.dirname(__file__), "output", "output.png")))

    return True

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 4:
        print("usage: python main.py x1 y1 x2 y2")
        print("example: python main.py 0 0 5 5")
        sys.exit(1)

    for arg in args:
        if not arg.isdigit():
            print("error: all arguments must be integers")
            sys.exit(1)

    start = Coordinates(int(args[0]), int(args[1]))
    end = Coordinates(int(args[2]), int(args[3]))

    r = main(start, end)
    if not r:
        sys.exit(1)
    sys.exit(0)
