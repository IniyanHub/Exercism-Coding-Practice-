def classify(n: int) -> str:
    if n < 1:
        raise ValueError("Classification is only possible for positive integers.")

    # Find aliquot sum
    aliquot_sum = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i != n:
                aliquot_sum += i
            if i != 1 and i * i != n:
                aliquot_sum += n // i

    # Classification
    if aliquot_sum == n:
        return "perfect"
    elif aliquot_sum > n:
        return "abundant"
    else:
        return "deficient"