def check_palindrome(user_input):
    int_list = []
    while user_input > 0:
        digit = user_input % 10
        user_input //= 10
        int_list.append(digit)
    begin = 0
    end = len(int_list) - 1
    while begin < end:
        if int_list[begin] == int_list[end]:
            begin += 1
            end -= 1
        else:
            return False
    return True