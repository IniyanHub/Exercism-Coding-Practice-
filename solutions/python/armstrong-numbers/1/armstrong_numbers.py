def is_armstrong_number(number):
    """Determine if a number is an Armstrong number.

    An Armstrong number is a number that is the sum of its own digits
    each raised to the power of the number of digits.

    :param number: int - The number to check.
    :return: bool - True if the number is an Armstrong number, False otherwise.
    """
    # Convert the number to a string to easily iterate over digits
    # and count the number of digits.
    digits = str(number)
    num_digits = len(digits)

    # Calculate the sum of digits each raised to the power of the count
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)

    # Check if the calculated sum matches the original number
    return armstrong_sum == number