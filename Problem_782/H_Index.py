def h_index(array):
    index = 0
    for i in range(1, len(array) + 1):
        temp = 0
        for j in range(len(array)):
            if array[j] >= i:
                temp += 1
        if temp >= i:
            index = temp
        else:
            break
    return index