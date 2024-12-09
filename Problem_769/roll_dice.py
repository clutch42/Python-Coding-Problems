import random


def number_of_tries(numbers, test_rolls):
    total_rolls = 0
    for i in range(test_rolls):
        total_rolls += roll_dice(numbers)
    return total_rolls / test_rolls


def roll_dice(numbers):
    i = 0
    tries = 1
    while i < len(numbers):
        if random_number_match(numbers[i]):
            i += 1
        else:
            tries += 1
            i = 0
    return tries


def random_number_match(number):
    if random.randint(1, 6) == number:
        return True
    return False
