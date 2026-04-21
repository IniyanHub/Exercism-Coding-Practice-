def encode(plain_text):
    result = []

    for c in plain_text.lower():
        if c.isalpha():
            result.append(chr(ord('z') - (ord(c) - ord('a'))))
        elif c.isdigit():
            result.append(c)
        # ignore punctuation

    transformed = "".join(result)

    # group into chunks of 5
    grouped = []
    for i in range(0, len(transformed), 5):
        grouped.append(transformed[i:i+5])

    return " ".join(grouped)


def decode(ciphered_text):
    result = []

    for c in ciphered_text.lower():
        if c.isalpha():
            result.append(chr(ord('z') - (ord(c) - ord('a'))))
        elif c.isdigit():
            result.append(c)
        # ignore spaces and punctuation

    return "".join(result)