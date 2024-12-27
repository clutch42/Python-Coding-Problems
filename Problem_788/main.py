# Write a program that checks whether an integer is a palindrome. For example, 121 is a palindrome, as well as 888.
# 678 is not a palindrome. Do not convert the integer into a string.
from Check_Palindrome import check_palindrome

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        user_input = input("Enter an integer: ")
        try:
            user_input_int = int(user_input)
        except ValueError:
            print("Not an integer")
        else:
            break

    print(f"{user_input_int} is a palindrome" if check_palindrome(user_input_int) else f"{user_input_int} is not a palindrome")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
