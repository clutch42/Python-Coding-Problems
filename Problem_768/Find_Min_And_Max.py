comparisons = 0
min_list = []
max_list = []


def find_min_and_max(list_of_numbers):
    global comparisons
    comparisons += 1
    if len(list_of_numbers) % 2 == 0:
        for i in range(0, len(list_of_numbers), 2):
            add_min_max(list_of_numbers[i], list_of_numbers[i+1])
        print(f"Min: {min_list} Max: {max_list}")
        minimum = find_min(min_list)
        maximum = find_max(max_list)
    else:
        for i in range(0, len(list_of_numbers)-1, 2):
            add_min_max(list_of_numbers[i], list_of_numbers[i+1])
        print(f"Min: {min_list} Max: {max_list}")
        minimum = find_min(min_list)
        maximum = find_max(max_list)
        comparisons += 2
        if list_of_numbers[-1] < minimum:
            minimum = list_of_numbers[-1]
        if list_of_numbers[-1] > maximum:
            maximum = list_of_numbers[-1]
    return minimum, maximum, comparisons


def add_min_max(a, b):
    global comparisons
    comparisons += 1
    if a < b:
        min_list.append(a)
        max_list.append(b)
    else:
        min_list.append(b)
        max_list.append(a)


def find_min(lst):
    global comparisons
    minimum = lst[0]
    for i in range(1, len(lst)):
        comparisons += 1
        if lst[i] < minimum:
            minimum = lst[i]
    return minimum


def find_max(lst):
    global comparisons
    maximum = lst[0]
    for i in range(1, len(lst)):
        comparisons += 1
        if lst[i] > maximum:
            maximum = lst[i]
    return maximum
