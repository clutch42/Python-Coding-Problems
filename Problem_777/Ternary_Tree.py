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

    def insert(self, word):
        if len(word) == 0:
            return False
        if self.root is None:
            self.root = Node(word[0])
        return self._insert(word, self.root)

    def _insert(self, word, node):
        if len(word) == 0:
            return True
        if node is None:
            node = Node(word[0])
        if node.value == word[0]:
            if node.center is None:
                node.center = Node(word[1]) if len(word) > 1 else None
            return self._insert(word[1:], node.center)
        if node.value > word[0]:
            if node.left is None:
                node.left = Node(word[0])
            return self._insert(word, node.left)
        if node.value < word[0]:
            if node.right is None:
                node.right = Node(word[0])
            return self._insert(word, node.right)

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
