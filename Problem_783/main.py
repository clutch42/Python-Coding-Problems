# Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does
# not necessarily have to be contiguous.
#
# For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing
# subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
from Find_Longest_Increasing import find_longest_increasing

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    array = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    print(array)
    new_array = find_longest_increasing(array)
    print(f"{new_array} length: {len(new_array)}")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
