def find_longest_increasing(array, last_value=-float('inf')):
    if not array:
        return []

    list_of_max = []
    for index, element in enumerate(array):
        if element > last_value:
            subsequent = [element] + find_longest_increasing(array[index + 1:], element)
            list_of_max.append(subsequent)

    if list_of_max:
        return max(list_of_max, key=len)
    else:
        return []
