def abbreviate(words):
    import re
    
    # Replace hyphens with spaces
    words = words.replace('-', ' ')
    
    # Keep words with apostrophes together
    word_list = re.findall(r"[A-Za-z']+", words)
    
    # Build acronym (ignore standalone apostrophes)
    return ''.join(word[0].upper() for word in word_list if word[0].isalpha())