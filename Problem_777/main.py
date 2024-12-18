# A ternary search tree is a trie-like data structure where each node may have up to three children. Here is an example which represents the words code, cob, be, ax, war, and we.
#
#        c
#     /  |  \
#    b   o   w
#  / |   |   |
# a  e   d   a
# |    / |   | \
# x   b  e   r  e
# The tree is structured according to the following rules:
#
# left child nodes link to words lexicographically earlier than the parent prefix
# right child nodes link to words lexicographically later than the parent prefix
# middle child nodes continue the current word
# For instance, since code is the first word inserted in the tree, and cob lexicographically precedes cod, cob is represented as a left child extending from cod.
#
# Implement insertion and search functions for a ternary search tree.
from Ternary_Tree import TernaryTree, print_tree

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    user_tree = TernaryTree()
    while True:
        print_tree(user_tree.root)
        print("1. Insert word")
        print("2. Search for word")
        print("3. Exit")
        user = input("Enter choice: ")
        if user == "3":
            break
        elif user == "1":
            word_insert = input("Enter word to insert to tree: ")
            if user_tree.insert(word_insert):
                print(f"{word_insert} inserted in tree.")
            else:
                print(f"{word_insert} not inserted in tree.")
        elif user == "2":
            word_search = input("Enter word to search for: ")
            if user_tree.search(word_search):
                print(f"{word_search} found in tree.")
            else:
                print(f"{word_search} not found in tree.")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
