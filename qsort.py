def qsort(value):
    if len(value) < 2:
        return value
    pivot = value[0]
    left = [x for x in value[1:] if x <= pivot]
    right = [x for x in value[1:] if x > pivot]
    return qsort(left) + [pivot] + qsort(right)
