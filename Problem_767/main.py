# Given a word W and a string S, find all starting indices in S which are anagrams of W.
# For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.

from find_anagram_indexes import find_anagram_indexes

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    word = input("Enter word: ")
    string = input("Enter anagram to find indexes of: ")
    arrayIndexes = find_anagram_indexes(word, string)
    for index in arrayIndexes:
        print(index)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
