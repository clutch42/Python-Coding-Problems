def map_words(word1, word2):
    if len(word1) != len(word2):
        return False
    letter_dict = {}
    for i in range(len(word1)):
        if word1[i] in letter_dict:
            if letter_dict[word1[i]] == word2[i]:
                continue
            else:
                return False
        else:
            letter_dict[word1[i]] = word2[i]
    print(letter_dict)
    return True
