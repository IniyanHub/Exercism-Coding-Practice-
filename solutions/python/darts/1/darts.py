import math

def score(x: float, y: float) -> int:
    """
    Calculate the points scored by a dart landing at coordinates (x, y).

    The target consists of three concentric circles centered at (0,0):
        - inner circle radius 1   → 10 points
        - middle circle radius 5  → 5 points
        - outer circle radius 10  → 1 point
    Points are 0 if the dart lands outside the outer circle.
    """
    distance = math.hypot(x, y)   # sqrt(x*x + y*y)

    if distance <= 1:
        return 10
    elif distance <= 5:
        return 5
    elif distance <= 10:
        return 1
    else:
        return 0