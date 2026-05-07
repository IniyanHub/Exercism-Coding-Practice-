from itertools import combinations as comb

def combinations(target, size, exclude):
    result = []

    # Digits from 1 to 9 excluding restricted digits
    digits = [d for d in range(1, 10) if d not in exclude]

    # Generate combinations
    for c in comb(digits, size):
        if sum(c) == target:
            result.append(list(c))

    return sorted(result)