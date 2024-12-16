class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.center = None
        self.left = None


def make_array(word):
    word_array = []
    for letter in word:
        word_array.append(letter)
    return word_array


def print_tree(node, level=0):
    if node is not None:
        # Print the current node's value
        print(" " * (level * 4) + f"Node: {node.value}")

        # Recursively print the left, center, and right children
        if node.left:
            print(" " * (level * 4) + "Left child:")
            print_tree(node.left, level + 1)

        if node.center:
            print(" " * (level * 4) + "Center child:")
            print_tree(node.center, level + 1)

        if node.right:
            print(" " * (level * 4) + "Right child:")
            print_tree(node.right, level + 1)


class TernaryTree:
    def __init__(self):
        self.root = None

    def insert2(self, word):
        word_array = make_array(word)
        if not word_array:
            return False
        if self.root is None:
            self.root = Node(word_array[0])

        index = 0
        current_node = self.root
        previous = None

        while index < len(word_array):
            char = word_array[index]
            if current_node is None:
                current_node = Node(char)
                if previous.value == word_array[index-1]:
                    previous.center = current_node
                elif previous.value > word_array[index-1]:
                    previous.right = current_node
                elif previous.value < word_array[index-1]:
                    previous.left = current_node
            elif char == current_node.value:
                previous = current_node
                current_node = current_node.center
                index += 1
            elif char < current_node.value:
                previous = current_node
                current_node = current_node.left
            elif char > current_node.value:
                previous = current_node
                current_node = current_node.right
        return True

    def insert(self, word):
        word_array = make_array(word)
        if self.root is None:
            self.root = Node(word_array[0])
        index = 0
        current_node = self.root
        while index < len(word_array):
            if current_node.center is None and word_array[index] == current_node.value:
                print("branch 1")
                index += 1
                if index < len(word_array):
                    current_node.center = Node(word_array[index])
                    current_node = current_node.center
            elif current_node.center is None and current_node.right is None and current_node.left is None:
                print("branch 2")
                current_node.center = Node(word_array[index])
                index += 1
                current_node = current_node.center
            elif current_node.center is not None and word_array[index] == current_node.value:
                print("branch 3")
                current_node = current_node.center
                index += 1
            elif word_array[index] < current_node.value:
                print("branch 4")
                if current_node.left is None:
                    current_node.left = Node(word_array[index])
                    index += 1
                current_node = current_node.left
            elif word_array[index] > current_node.value:
                print("branch 5")
                if current_node.right is None:
                    current_node.right = Node(word_array[index])
                    index += 1
                current_node = current_node.right
        return True

    def search(self, word):
        word_array = make_array(word)
        current_node = self.root
        index = 0
        while index < len(word_array):
            if current_node is None:
                return False
            elif word_array[index] == current_node.value:
                index += 1
                current_node = current_node.center
            elif word_array[index] < current_node.value:
                if current_node.left is None:
                    return False
                current_node = current_node.left
                if current_node.value == word_array[index]:
                    index += 1
            else:
                if current_node.right is None:
                    return False
                current_node = current_node.right
                if current_node.value == word_array[index]:
                    index += 1
        return True
