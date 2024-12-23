def string_in_matrix(user_input, matrix):
    for i, row in enumerate(matrix):
        word_index = 0
        for j, letter in enumerate(row):
            if matrix[i][j] == user_input[word_index]:
                word_index += 1
                if len(user_input) == word_index:
                    return True
            else:
                word_index = 0
    for j, column in enumerate(matrix):
        word_index = 0
        for i, letter in enumerate(row):
            if matrix[i][j] == user_input[word_index]:
                word_index += 1
                if len(user_input) == word_index:
                    return True
            else:
                word_index = 0
    return False
