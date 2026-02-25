def eat_ghost(power_pellet_active, touching_ghost):
    """
    Return True if Pac-Man eats a ghost.
    Pac-Man eats a ghost if he has a power pellet active and is touching a ghost.
    """
    return power_pellet_active and touching_ghost


def score(touching_power_pellet, touching_dot):
    """
    Return True if Pac-Man scores.
    Pac-Man scores if he is touching a power pellet or a dot.
    """
    return touching_power_pellet or touching_dot


def lose(power_pellet_active, touching_ghost):
    """
    Return True if Pac-Man loses.
    Pac-Man loses if he is touching a ghost and does not have a power pellet active.
    """
    return touching_ghost and not power_pellet_active


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """
    Return True if Pac-Man wins.
    Pac-Man wins if he has eaten all of the dots and has not lost.
    """
    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)