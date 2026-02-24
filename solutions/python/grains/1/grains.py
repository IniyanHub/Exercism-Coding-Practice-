"""Module for calculating grains of wheat on a chessboard."""

def square(number):
    """Calculate the number of grains on a specific square.

    :param number: int - The square number (1-64).
    :return: int - The number of grains on that square.
    :raises ValueError: If the square number is not between 1 and 64.
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    
    # The number of grains doubles for each square, starting with 1 on square 1.
    # This is equivalent to 2^(number - 1).
    return 2 ** (number - 1)


def total():
    """Calculate the total number of grains on the chessboard.

    :return: int - Total grains on all 64 squares.
    """
    # The sum of 2^0 + 2^1 + ... + 2^63 is equal to 2^64 - 1.
    return (2 ** 64) - 1