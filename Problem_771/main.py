# Determine whether there exists a one-to-one character mapping from one string s1 to another s2.

# For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.

# Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.

# Press the green button in the gutter to run the script.

from map_words import map_words


if __name__ == '__main__':
    word1 = input("Enter word 1: ")
    word2 = input("Enter word 2: ")
    if map_words(word1, word2):
        print(f"{word1} maps to {word2}")
    else:
        print(f"{word1} does not map to {word2}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
