import math


def square(rad, is3d=False, fix=2):
    if rad < 0:
        return "radius should be positive number"

    fix_str = f"%.{fix}f"

    if is3d:
        return fix_str % ((4 * math.pi * (rad ** 3)) / 3)
    return fix_str % (math.pi * (rad ** 2))
