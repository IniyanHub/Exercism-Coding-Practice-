def _is_valid_triangle(a, b, c):
    """
    Helper function to determine if the sides form a valid triangle.
    A triangle is valid if all sides are greater than 0 and the sum
    of any two sides is greater than the third.
    """
    # Check for positive sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    # Check triangle inequality theorem
    # We use strict inequality (>) to exclude degenerate triangles 
    # as per the exercise note to ignore them.
    return (a + b > c) and (a + c > b) and (b + c > a)


def equilateral(sides):
    """
    An equilateral triangle has all three sides the same length.
    """
    a, b, c = sides
    return _is_valid_triangle(a, b, c) and a == b == c


def isosceles(sides):
    """
    An isosceles triangle has at least two sides the same length.
    """
    a, b, c = sides
    return _is_valid_triangle(a, b, c) and (a == b or b == c or a == c)


def scalene(sides):
    """
    A scalene triangle has all sides of different lengths.
    """
    a, b, c = sides
    return _is_valid_triangle(a, b, c) and a != b and b != c and a != c