def maximum_product(integer_list):
    if len(integer_list) < 3:
        return 0
    integer_list = sorted(integer_list)
    product = 1
    if integer_list[-1] < 0 or integer_list[0] > 0:
        for i in range(len(integer_list)-3, len(integer_list)):
            product *= integer_list[i]
    elif integer_list[0] * integer_list[1] > integer_list[len(integer_list)-3] * integer_list[len(integer_list) - 2]:
        product *= integer_list[0] * integer_list[1] * integer_list[-1]
    else:
        product *= integer_list[len(integer_list)-3] * integer_list[len(integer_list) - 2] * integer_list[len(integer_list) - 1]
    return product