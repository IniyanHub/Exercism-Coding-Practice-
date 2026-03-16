def is_pangram(sentence):
    """
    Determines if a sentence is a pangram using a bitmask for high performance.
    A pangram contains every letter of the alphabet at least once.
    """
    # 'seen' is an integer where each bit represents a letter in the alphabet.
    # Bit 0 represents 'a', Bit 1 represents 'b', ..., Bit 25 represents 'z'.
    seen = 0
    
    for char in sentence:
        # Check if the character is an uppercase letter
        if 'A' <= char <= 'Z':
            # Convert to 0-25 index and set the corresponding bit
            seen |= 1 << (ord(char) - ord('A'))
        # Check if the character is a lowercase letter
        elif 'a' <= char <= 'z':
            # Convert to 0-25 index and set the corresponding bit
            seen |= 1 << (ord(char) - ord('a'))
    
    # (1 << 26) - 1 creates a number where the first 26 bits are 1.
    # If 'seen' equals this number, all letters have been found.
    return seen == (1 << 26) - 1