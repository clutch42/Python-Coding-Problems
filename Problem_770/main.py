# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
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
