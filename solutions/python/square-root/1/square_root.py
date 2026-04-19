def square_root(n: int) -> int:
    left, right = 1, n

    while left <= right:
        mid = (left + right) // 2
        square = mid * mid

        if square == n:
            return mid
        elif square < n:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # should not happen as per problem guarantee