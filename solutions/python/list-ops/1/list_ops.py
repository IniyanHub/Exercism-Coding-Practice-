def append(list1, list2):
    result = []
    for item in list1:
        result += [item]
    for item in list2:
        result += [item]
    return result


def concat(lists):
    result = []
    for lst in lists:
        for item in lst:
            result += [item]
    return result


def filter(function, list):
    result = []
    for item in list:
        if function(item):
            result += [item]
    return result


def length(list):
    count = 0
    for _ in list:
        count += 1
    return count


def map(function, list):
    result = []
    for item in list:
        result += [function(item)]
    return result


def foldl(function, list, initial):
    acc = initial
    for item in list:
        acc = function(acc, item)
    return acc


def foldr(function, list, initial):
    acc = initial
    for i in range(length(list) - 1, -1, -1):
        acc = function(acc, list[i])   # ✅ FIXED ORDER
    return acc


def reverse(list):
    result = []
    for item in list:
        result = [item] + result
    return result