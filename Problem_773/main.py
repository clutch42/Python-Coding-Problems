# We can determine how "out of order" an array A is by counting the number of inversions it has.
# Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller
# element appears after a larger element.
# Given an array, count the number of inversions it has. Do this faster than O(N^2) time.
#
# You may assume each element in the array is distinct.
#
# For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has
# three inversions: (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has
# ten inversions: every distinct pair forms an inversion.
from Inversion import find_inversions

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    num_array = []
    while True:
        user_input = input("Enter numbers for array or end to finish: ")
        if user_input == "end":
            break
        try:
            to_number = int(user_input)
            num_array.append(to_number)
        except ValueError:
            print("Must be an integer")
    print(find_inversions(num_array))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
