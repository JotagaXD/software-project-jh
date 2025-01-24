from numpy import arctan, degrees

def angle(n: float, dx: float, dy: float):
    angle = degrees(arctan(n))
    if dx < 0 and dy > 0:
        angle = -angle
        angle += 90
    elif dx < 0 and dy < 0:
        angle += 180
    elif dx > 0 and dy < 0:
        angle = -angle
        angle += 270
    return angle

def distance(init: tuple, destiny: tuple):
    return (((init[0] - destiny[0])**2) + ((init[1] - destiny[1])**2))**(1/2)

def angular_coef(dy, dx):
    return dy / dx

def linear_coef(a: float, coord: tuple):
    return coord[1] - a*coord[0]

def relative_x(condition: bool, angle: float, x1):
    if condition:
        if 270 < angle and angle <= 360:
            return x1 - 1
        elif 0 < angle and angle <= 90:
            return x1 + 1
        if 90 < angle and angle <= 180:
            return x1 - 1
        elif 180 < angle and angle <= 270:
            return x1 + 1
    else:
        if 270 < angle and angle <= 360:
            return x1 + 1
        elif 0 < angle and angle <= 90:
            return x1 - 1
        if 90 < angle and angle <= 180:
            return x1 + 1
        elif 180 < angle and angle <= 270:
            return x1 - 1
