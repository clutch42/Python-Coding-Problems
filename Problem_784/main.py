# Given a 2D matrix of characters and a target word, write a function that returns whether
# the word can be found in the matrix by going left-to-right, or up-to-down.
#
# For example, given the following matrix:
#
# [['F', 'A', 'C', 'I'],
#  ['O', 'B', 'Q', 'P'],
#  ['A', 'N', 'O', 'B'],
#  ['M', 'A', 'S', 'S']]
# and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly,
# given the target word 'MASS', you should return true, since it's the last row.
from String_In_Matrix import string_in_matrix

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    matrix = [['F', 'A', 'C', 'I'],
              ['O', 'B', 'Q', 'P'],
              ['A', 'N', 'O', 'B'],
              ['M', 'A', 'S', 'S']]
    for row in matrix:
        print(row)
    user_input = input('Enter word to find up to down or left to right, case insensitive: ').upper()
    print(f"{user_input} is{' not' if not string_in_matrix(user_input, matrix) else ''} in the matrix")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
