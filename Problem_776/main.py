# There are N prisoners standing in a circle, waiting to be executed. The executions are
# carried out starting with the kth person, and removing every successive kth person going
# clockwise until there is no one left.
# Given N and k, write an algorithm to determine where a prisoner should stand in order to
# be the last survivor.
# For example, if N = 5 and k = 2, the order of executions would be [2, 4, 1, 5, 3], so you
# should return 3.
# Bonus: Find an O(log N) solution if k = 2.
from Last_Executed import last_executed

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        n = input("Enter number of prisoners: ")
        try:
            n = int(n)
            break
        except ValueError:
            print("Enter an integer")
    while True:
        k = input("Enter number of prisoners to skip: ")
        try:
            k = int(k)
            break
        except ValueError:
            print("Enter an integer")
    print(f"Prisoners: {n} Number to skip: {k}")
    print(f"Last prisoner executed: {last_executed(n, k)}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
