# You have access to ranked lists of songs for various users. Each song is represented as an integer, and more
# preferred songs appear earlier in each list. For example, the list [4, 1, 7] indicates that a user likes song
# 4 the best, followed by songs 1 and 7.
# Given a set of these ranked lists, interleave them to create a playlist that satisfies everyone's priorities.
# For example, suppose your input is {[1, 7, 3], [2, 1, 6, 7, 9], [3, 9, 5]}. In this case a satisfactory playlist
# could be [2, 1, 6, 7, 3, 9, 5].
from Merge_Lists import merge_lists

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Enter playlists")
    playlists = []
    userlist = []
    while True:
        user = input("Enter number or end to finish or next to enter next playlist: ")
        if user == "end":
            playlists.append(userlist)
            break
        elif user == "next":
            playlists.append(userlist)
            userlist = []
        else:
            try:
                userlist.append(int(user))
            except ValueError:
                print("enter a integer")
    print(playlists)
    print(merge_lists(playlists))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
