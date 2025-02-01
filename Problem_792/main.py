# You have N stones in a row, and would like to create from them a pyramid. This pyramid should be constructed such that
# the height of each stone increases by one until reaching the tallest stone, after which the heights decrease by one.
# In addition, the start and end stones of the pyramid should each be one stone high.
#
# You can change the height of any stone by paying a cost of 1 unit to lower its height by 1, as many times as necessary.
# Given this information, determine the lowest cost method to produce this pyramid.
#
# For example, given the stones [1, 1, 3, 3, 2, 1], the optimal solution is to pay 2 to create [0, 1, 2, 3, 2, 1].
from Find_New_Heights import get_new_heights

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    heights = []
    while True:
        new_input = input("Enter heights or end to finish: ")
        if new_input == "end":
            break
        try:
            heights.append(int(new_input))
        except ValueError:
            print("Enter an integer")
    print(heights)
    new_heights = get_new_heights(heights)
    print(f"You need to remove {new_heights[0]} to get {new_heights[1]}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
