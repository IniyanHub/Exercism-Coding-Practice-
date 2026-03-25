def rotate(text, key):
    """
    Encrypts a text using the rotational cipher (Caesar cipher).
    
    Args:
        text (str): The input string to encrypt.
        key (int): The number of positions to shift letters.
        
    Returns:
        str: The encrypted string.
    """
    # Normalize key to handle values > 26 or < 0
    key = key % 26
    result = []

    for char in text:
        if char.isupper():
            # Shift uppercase letters
            shifted_char = chr((ord(char) - 65 + key) % 26 + 65)
            result.append(shifted_char)
        elif char.islower():
            # Shift lowercase letters
            shifted_char = chr((ord(char) - 97 + key) % 26 + 97)
            result.append(shifted_char)
        else:
            # Keep spaces, punctuation, and numbers unchanged
            result.append(char)

    return "".join(result)