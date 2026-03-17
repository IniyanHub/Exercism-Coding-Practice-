def is_isogram(string):
    """
    Determines if a word or phrase is an isogram.
    
    An isogram is a word or phrase without a repeating letter. 
    This check is case-insensitive and ignores spaces and hyphens.
    """
    # Convert to lowercase to handle case insensitivity
    clean_string = string.lower()
    
    # Create a set to track seen letters
    seen_letters = set()
    
    for char in clean_string:
        # Ignore spaces and hyphens
        if char == ' ' or char == '-':
            continue
        
        # If the character is already in the set, it's a repeat
        if char in seen_letters:
            return False
        
        # Add the character to the set
        seen_letters.add(char)
        
    # If no repeats were found, return True
    return True