def encode(numbers):
    result = []

    for num in numbers:
        if num < 0:
            raise ValueError("only non-negative integers allowed")

        parts = []

        # Extract 7-bit chunks
        while True:
            parts.append(num & 0x7F)
            num >>= 7
            if num == 0:
                break

        # Reverse and set continuation bits
        for i in range(len(parts) - 1, -1, -1):
            byte = parts[i]
            if i != 0:
                byte |= 0x80  # set MSB (continuation bit)
            result.append(byte)

    return result


def decode(bytes_):
    result = []
    current = 0
    in_progress = False

    for byte in bytes_:
        in_progress = True

        current = (current << 7) | (byte & 0x7F)

        # If MSB = 0 → end of one number
        if (byte & 0x80) == 0:
            result.append(current)
            current = 0
            in_progress = False

    # If still expecting more bytes → error
    if in_progress:
        raise ValueError("incomplete sequence")

    return result