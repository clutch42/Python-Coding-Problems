# In academia, the h-index is a metric used to calculate the impact of a researcher's papers. It is calculated as follows:
# A researcher has index h if at least h of her N papers have h citations each. If there are multiple h satisfying this
# formula, the maximum is chosen.
# For example, suppose N = 5, and the respective citations of each paper are [4, 3, 0, 1, 5]. Then the h-index would be
# 3, since the researcher has 3 papers with at least 3 citations.
# Given a list of paper citations of a researcher, calculate their h-index.
from H_Index import h_index

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    integer_list = []
    while True:
        user = input("Enter integer or end to finish: ")
        if user == "end":
            break
        try:
            integer_list.append(int(user))
        except ValueError:
            print("Enter an integer")
    print(integer_list)
    print(f"The h index of the list is: {h_index(integer_list)}")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
