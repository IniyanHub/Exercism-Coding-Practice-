def translate(text):
    """
    Translates a text string into Pig Latin based on the specified rules.
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    words = text.split()
    result = []

    for word in words:
        # Rule 1: If a word begins with a vowel, or starts with "xr" or "yt", add "ay" to the end.
        if word[0] in vowels or word.startswith('xr') or word.startswith('yt'):
            result.append(word + 'ay')
            continue

        # Rules 2, 3, 4: Determine the prefix of consonants (and 'qu') to move.
        index = 0
        
        while index < len(word):
            # Rule 3: Special handling for 'qu'.
            # If we encounter 'q' and the next letter is 'u', we treat them as a unit.
            if word[index] == 'q' and index + 1 < len(word) and word[index + 1] == 'u':
                index += 2
                break
            
            # Rule 2: Stop if we hit a standard vowel.
            if word[index] in vowels:
                break
            
            # Rule 4: 'y' acts as a vowel if it is not the first letter.
            if word[index] == 'y' and index > 0:
                break
            
            # Otherwise, it is a consonant, so we include it in the prefix.
            index += 1

        # Separate the prefix and the stem, then recombine.
        prefix = word[:index]
        stem = word[index:]
        result.append(stem + prefix + 'ay')

    return ' '.join(result)
