def commands(binary_str):
    actions = [
        "wink",
        "double blink",
        "close your eyes",
        "jump"
    ]

    result = []

    # Reverse to process from rightmost bit
    binary_str = binary_str[::-1]

    for i in range(min(4, len(binary_str))):
        if binary_str[i] == '1':
            result.append(actions[i])

    # Check 5th bit for reversal
    if len(binary_str) > 4 and binary_str[4] == '1':
        result.reverse()

    return result