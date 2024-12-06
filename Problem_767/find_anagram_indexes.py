

def find_anagram_indexes(word, string):
    indexes = []
    difference = len(word) - len(string)
    if difference < 0:
        return ["Anagram too long"]
    if difference == 0:
        if compare_words(word, string):
            indexes.append(0)
        else:
            indexes.append("No anagrams")
        return indexes
    for index, char in enumerate(word[:difference+1]):
        if compare_words(word[index:index+len(string)], string):
            indexes.append(index)
    return indexes


def compare_words(word1, word2):
    if len(word1) != len(word2):
        return False
    for char in word1:
        word2 = word2.replace(char, "", 1)
    if len(word2) == 0:
        return True
    return False
