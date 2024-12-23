# Given a list of integers, return the largest product that can be made by multiplying any three integers.
# For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.
# You can assume the list has at least three integers.\
from Maximum_Product import maximum_product

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Return the largest product that can be made by multiplying any three integers in a list.")
    integer_list = []
    while True:
        user_input = input("Enter an integer or end to quit: ")
        if user_input == 'end':
            break
        try:
            integer_list.append(int(user_input))
        except ValueError:
            print("Enter an integer.")
    print(integer_list)
    print(f"Maximum product is {maximum_product(integer_list)}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
