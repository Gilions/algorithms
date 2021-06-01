def merge_sort(value):
    # Drop list
    if len(value) < 2:
        return value

    pivot = len(value) // 2
    left = merge_sort(value[:pivot])
    right = merge_sort(value[pivot:])
    return sorting(left, right)

def sorting(left, right):
    # Sorting
    answer = []

    i = j = 0
    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            answer.append(left[i])
            i += 1
        else:
            answer.append(right[j])
            j += 1
    if i < len(left):
        answer += left[i:]
    if j < len(right):
        answer += right[j:]
    return answer
