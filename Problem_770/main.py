# The game of Nim is played as follows. Starting with three heaps, each containing a variable
# number of items, two players take turns removing one or more items from a single pile. The
# player who eventually is forced to take the last stone loses. For example, if the initial
# heap sizes are 3, 4, and 5, a game could be played as shown below:
#   A  |  B  |  C
# -----------------
#   3  |  4  |  5
#   3  |  1  |  3
#   3  |  1  |  3
#   0  |  1  |  3
#   0  |  1  |  0
#   0  |  0  |  0
# In other words, to start, the first player takes three items from pile B. The second player
# responds by removing two stones from pile C. The game continues in this way until player one
# takes last stone and loses.
#
# Given a list of non-zero starting values [a, b, c], and assuming optimal play, determine whether
# the first player has a forced win.
from NimSum import PlayNim

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    user_list = []
    while True:
        user_input = input("Enter number for the pile or \"end\" to finish: ")
        try:
            input_num = int(user_input)
            if input_num > 0:
                user_list.append(int(user_input))
            else:
                print("Must be greater than 0")
        except ValueError:
            if user_input == "end":
                break
            print("Invalid value")
    game = PlayNim(user_list)
    player1 = game.current_player_wins()
    if player1:
        print("Player 1 should win.")
    else:
        print("Player 2 should win.")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
