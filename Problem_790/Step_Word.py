def step_word(word, dictionary):
    words = []
    for d in dictionary:
        letter_not_found = False
        temp_word = d
        for i in range(len(word)):
            if word[i] in temp_word:
                temp_word = temp_word.replace(word[i], "", 1)
            else:
                letter_not_found = True
                break
        if letter_not_found:
            continue
        if len(temp_word) == 1:
            words.append(d)
    return words