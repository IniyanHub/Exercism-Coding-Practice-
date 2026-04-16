def flatten(arr):
    result = []
    
    for item in arr:
        if isinstance(item, list):
            result.extend(flatten(item))
        elif item is not None:   # skip null
            result.append(item)
    
    return result