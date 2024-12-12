# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
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
