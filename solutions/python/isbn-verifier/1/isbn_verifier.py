def is_valid(isbn: str) -> bool:
    """
    Validates an ISBN-10 number.
    
    Args:
        isbn (str): The ISBN string to validate.
        
    Returns:
        bool: True if valid, False otherwise.
    """
    # Remove hyphens from the string
    clean_isbn = isbn.replace("-", "")
    
    # An ISBN-10 must have exactly 10 characters
    if len(clean_isbn) != 10:
        return False
    
    total_sum = 0
    
    for i in range(10):
        char = clean_isbn[i]
        
        # The check digit (last character) can be 'X' representing 10
        if i == 9 and char == 'X':
            value = 10
        # All other characters must be digits
        elif char.isdigit():
            value = int(char)
        else:
            return False
        
        # Add to the weighted sum
        # d1 * 10 + d2 * 9 + ... + d10 * 1
        # index 0 corresponds to d1 (weight 10), so weight is 10 - i
        total_sum += value * (10 - i)
        
    # If the sum is divisible by 11, it is valid
    return total_sum % 11 == 0