def find_anagrams(target, candidates):
    result = []
    target_lower = target.lower()
    target_sorted = sorted(target_lower)

    for word in candidates:
        word_lower = word.lower()

        # skip same word
        if word_lower == target_lower:
            continue

        if sorted(word_lower) == target_sorted:
            result.append(word)

    return result