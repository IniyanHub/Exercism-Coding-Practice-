def encode(string):
    if not string:
        return ""
    
    result = []
    count = 1
    
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            if count > 1:
                result.append(str(count))
            result.append(string[i - 1])
            count = 1
    
    # last group
    if count > 1:
        result.append(str(count))
    result.append(string[-1])
    
    return "".join(result)


def decode(string):
    result = []
    count = 0
    
    for ch in string:
        if ch.isdigit():
            count = count * 10 + int(ch)  # handle multi-digit counts
        else:
            if count == 0:
                count = 1
            result.append(ch * count)
            count = 0
    
    return "".join(result)