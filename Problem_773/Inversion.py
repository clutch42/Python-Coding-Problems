def find_inversions(num_array):
    inversions = []
    merge_sort(inversions, num_array)
    return inversions


def merge_sort(inversions, num_array):
    if len(num_array) <= 1:
        return num_array
    mid = len(num_array) // 2
    left_half = merge_sort(inversions, num_array[:mid])
    right_half = merge_sort(inversions, num_array[mid:])
    return merge(inversions, left_half, right_half)


def merge(inversions, left, right):
    sorted_array = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            for k in range(i, len(left)):
                inversions.append((left[k], right[j]))
            j += 1
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    return sorted_array
