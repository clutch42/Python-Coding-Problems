from Boggle_Letter_Node import LetterNode


class Boggle:
    def __init__(self, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p):
        self.board = [[LetterNode(a), LetterNode(b), LetterNode(c), LetterNode(d)],
                      [LetterNode(e), LetterNode(f), LetterNode(g), LetterNode(h)],
                      [LetterNode(i), LetterNode(j), LetterNode(k), LetterNode(l)],
                      [LetterNode(m), LetterNode(n), LetterNode(o), LetterNode(p)]]

    def print_board(self):
        for row in self.board:
            for character in row:
                print(character.letter, end=" ")
            print()

    def reset_used(self):
        for row in self.board:
            for letter in row:
                letter.used = False

    def index_exists(self, i, j):
        if 0 <= i <= 3 and 0 <= j <= 3 and not self.board[i][j].used:
            return True
        return False

    def word_exists(self, i, j, word):
        if not self.index_exists(i, j) or word[0] != self.board[i][j].letter:
            return False
        self.board[i][j].used = True
        if len(word) == 1:
            self.reset_used()
            return True
        found = self.word_exists(i + 1, j, word[1:]) or \
                self.word_exists(i - 1, j, word[1:]) or \
                self.word_exists(i, j + 1, word[1:]) or \
                self.word_exists(i, j - 1, word[1:])
        self.board[i][j].used = False
        return found

    def words_found(self, list_of_words):
        words = []
        for word in list_of_words:
            for i in range(len(self.board)):
                for j in range(len(self.board[0])):
                    if self.board[i][j].letter == word[0]:
                        if self.word_exists(i, j, word):
                            words.append(word)
        return words
