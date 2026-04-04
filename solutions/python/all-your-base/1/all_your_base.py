def rebase(input_base, digits, output_base):
    """
    Converts a sequence of digits from one base to another.
    """
    # Validate input base
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    # Validate output base
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    # Validate digits
    for digit in digits:
        if not (0 <= digit < input_base):
            raise ValueError("all digits must satisfy 0 <= d < input base")

    # Convert the digits to a decimal (base 10) integer
    number = 0
    for digit in digits:
        number = number * input_base + digit

    # Handle the edge case where the number is 0
    if number == 0:
        return [0]

    # Convert the decimal integer to the output base
    output_digits = []
    while number > 0:
        output_digits.append(number % output_base)
        number //= output_base

    # The digits are collected in reverse order (least significant first),
    # so we reverse the list before returning.
    return output_digits[::-1]