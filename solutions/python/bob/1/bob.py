def response(hey_bob):
    # Remove leading/trailing whitespace to handle inputs correctly
    trimmed = hey_bob.strip()
    
    # Rule 1: Silence (empty string or only whitespace)
    if not trimmed:
        return "Fine. Be that way!"
    
    # Determine flags for yelling and questions
    # is_yelling: True if there is at least one cased letter and all are uppercase
    is_yelling = trimmed.isupper() and any(c.isalpha() for c in trimmed)
    # is_question: True if the string ends with a question mark
    is_question = trimmed.endswith('?')
    
    # Rule 3: Yelling a question (takes priority over simple yelling or simple question)
    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    
    # Rule 2: Yelling
    if is_yelling:
        return "Whoa, chill out!"
    
    # Rule 4: Question
    if is_question:
        return "Sure."
    
    # Rule 5: Anything else
    return "Whatever."