"""
    Module that contains the Bresenham algorithm

    References:
        https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm
        https://sites.google.com/site/felipealvesaraujocg/trabalho1
"""


def bresenham(x0, y0, x1, y1):
    """
        Bresenham algorithm implementation

        Parameters:
            x0 (int): x0 point
            y0 (int): y0 point
            x1 (int): x1 point
            y1 (int): y1 point
    """

    dx = x1 - x0
    dy = y1 - y0

    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0

    D = 2*dy - dx
    y = 0

    for x in range(dx + 1):
        yield x0 + x*xx + y*yx, y0 + x*xy + y*yy
        if D >= 0:
            y += 1
            D -= 2*dx
        D += 2*dy
