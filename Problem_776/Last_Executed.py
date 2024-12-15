def last_executed(number_of_prisoners, number_to_skip):
    prisoners = list(range(1, number_of_prisoners + 1))
    order = [0] * number_of_prisoners
    index = number_to_skip % len(prisoners)
    current_execution = 1
    while len(prisoners) > 1:
        print(index)
        order[prisoners[index]-1] = current_execution
        current_execution += 1
        prisoners.pop(index)
        index = (index + number_to_skip) % len(prisoners)
    last = prisoners[0] - 1
    order[last] = current_execution
    return last, order


def last_if_k_is_2(n):
    largest_power_of_2 = 1 << (n.bit_length() - 1)
    print(largest_power_of_2)
    return 2*(n - largest_power_of_2) - 1
