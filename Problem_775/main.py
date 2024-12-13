# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
from find_rooms import find_rooms

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    times = []
    while True:
        start = input("Enter start time or end to continue: ")
        if start != "end":
            end = input("Enter end time: ")
        else:
            break
        try:
            times.append((int(start), int(end)))
        except ValueError:
            print("Times must be integers")
    print(times)
    print(f"Minimum rooms needed: {find_rooms(times)}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
