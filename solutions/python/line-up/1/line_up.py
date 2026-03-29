
def line_up(name: str, number: int) -> str:
    """
    Generates a ticket string for a customer with their name and ordinal position.
    """
    # Determine the last digit and the last two digits
    remainder_10 = number % 10
    remainder_100 = number % 100
    
    # Apply the rules for ordinal suffixes
    if 11 <= remainder_100 <= 13:
        suffix = "th"
    elif remainder_10 == 1:
        suffix = "st"
    elif remainder_10 == 2:
        suffix = "nd"
    elif remainder_10 == 3:
        suffix = "rd"
    else:
        suffix = "th"
        
    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"