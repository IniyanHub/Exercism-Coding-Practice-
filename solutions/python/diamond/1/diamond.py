def rows(letter: str) -> list[str]:
    n = ord(letter) - ord('A')
    result = []
    
    # Top half (including middle)
    for i in range(n + 1):
        ch = chr(ord('A') + i)
        outer_spaces = n - i
        
        if i == 0:
            row = ' ' * outer_spaces + ch + ' ' * outer_spaces
        else:
            inner_spaces = 2 * i - 1
            row = (
                ' ' * outer_spaces +
                ch +
                ' ' * inner_spaces +
                ch +
                ' ' * outer_spaces
            )
        result.append(row)
    
    # Bottom half (mirror)
    for i in range(n - 1, -1, -1):
        result.append(result[i])
    
    return result