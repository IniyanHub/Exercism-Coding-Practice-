def annotate(garden):
    # Validate input
    if not isinstance(garden, list):
        raise ValueError("The board is invalid with current input.")

    if len(garden) == 0:
        return []

    row_length = len(garden[0])

    for row in garden:
        if len(row) != row_length:
            raise ValueError("The board is invalid with current input.")

        for ch in row:
            if ch not in (' ', '*'):
                raise ValueError("The board is invalid with current input.")

    rows = len(garden)
    cols = row_length

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    result = []

    for i in range(rows):
        new_row = ""

        for j in range(cols):
            if garden[i][j] == '*':
                new_row += '*'
            else:
                count = 0

                for dx, dy in directions:
                    ni = i + dx
                    nj = j + dy

                    if 0 <= ni < rows and 0 <= nj < cols:
                        if garden[ni][nj] == '*':
                            count += 1

                if count == 0:
                    new_row += ' '
                else:
                    new_row += str(count)

        result.append(new_row)

    return result