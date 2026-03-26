RESISTOR_COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white"
]

def color_code(color):
    """
    Returns the numerical value associated with a particular color band.
    """
    return RESISTOR_COLORS.index(color)

def colors():
    """
    Returns the list of all possible band colors.
    """
    # Return a copy of the list to prevent accidental modification of the constant
    return list(RESISTOR_COLORS)