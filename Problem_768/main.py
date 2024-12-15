# Given an array of numbers of length N, find both the minimum and maximum using
# less than 2 * (N - 2) comparisons.
from Find_Min_And_Max import find_min_and_max

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list_of_nums = []
    while True:
        num = input("Enter integer or end when finished: ")
        if num == "end":
            break
        try:
            list_of_nums.append(int(num))
        except ValueError:
            print("Must be integer")
    print(list_of_nums)
    answer = find_min_and_max(list_of_nums)
    print(f"Min: {answer[0]} Max: {answer[1]} Comparisons: {answer[2]}")
    print(f"2 * (N - 2) = {2*(len(list_of_nums)-2)}")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
