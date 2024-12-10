# This is a sample Python script.

# Boggle is a game played on a 4 x 4 grid of letters. The goal is to find as many words as possible that can be
# formed by a sequence of adjacent letters in the grid, using each cell at most once. Given a game board and a
# dictionary of valid words, implement a Boggle solver.
from Boggle import Boggle


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    boggle_board = Boggle('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p')
    boggle_board.print_board()
    list_of_words = []
    while True:
        word = input("Enter word in dictionary or \"end\" to finish: ")
        if word != "end":
            list_of_words.append(word)
        else:
            break
    print(list_of_words)
    words = boggle_board.words_found(list_of_words)
    print(words)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
