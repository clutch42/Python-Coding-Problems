def get_new_heights(height_list):
    new_heights = []
    total_removed = float('inf')
    maximum_height = len(height_list) - (len(height_list) // 2)
    for i in range(len(height_list)):
        temp_total_removed = 0
        temp_new_heights = [0] * len(height_list)
        if i+1 < maximum_height:
            index_maximum_height = i+1
        elif len(height_list) - i < maximum_height:
            index_maximum_height = len(height_list) - i
        else:
            index_maximum_height = maximum_height
        if height_list[i] > index_maximum_height:
            temp_total_removed += height_list[i] - index_maximum_height
            temp_new_heights[i] = index_maximum_height
        else:
            temp_new_heights[i] = height_list[i]


        # right_index = i
        # left_index = i
        # right_index_height = temp_new_heights[i]
        # left_index_height = temp_new_heights[i]

        def valid_index(index):
            if 0 <= index < len(height_list):
                return True
            return False

        def remove_right():
            nonlocal temp_total_removed
            right_index = i
            right_index_height = temp_new_heights[i]
            while right_index_height != 1:
                if valid_index(right_index + 1) and right_index_height <= height_list[right_index + 1] + 1:
                    temp_total_removed += height_list[right_index + 1] - right_index_height + 1
                    right_index += 1
                    right_index_height -= 1
                    temp_new_heights[right_index] = right_index_height
                else:
                    while right_index_height > height_list[right_index + 1] + 1:
                        right_index_height -= 1
                        for j in range(i, right_index+1):
                            temp_total_removed += 1
                            temp_new_heights[j] -= 1
            right_index += 1
            while right_index < len(height_list):
                print(right_index)
                temp_total_removed += height_list[right_index]
                right_index += 1

        def remove_left():
            nonlocal temp_total_removed
            left_index = i
            left_index_height = temp_new_heights[i]
            while left_index_height != 1:
                if valid_index(left_index + 1) and left_index_height <= height_list[left_index - 1] + 1:
                    temp_total_removed += height_list[left_index - 1] - left_index_height + 1
                    left_index -= 1
                    left_index_height -= 1
                    temp_new_heights[left_index] = left_index_height
                else:
                    while left_index_height > height_list[left_index - 1] + 1:
                        left_index_height -= 1
                        for j in range(left_index, i+1):
                            temp_total_removed += 1
                            temp_new_heights[j] -= 1
            left_index -= 1
            while left_index >= 0:
                temp_total_removed += height_list[left_index]
                left_index -= 1

        right = i + 1
        left = i - 1
        if valid_index(right) and valid_index(left) and height_list[right] < height_list[left]:
            remove_right()
            remove_left()
        else:
            remove_left()
            remove_right()

        if temp_total_removed < total_removed:
            total_removed = temp_total_removed
            new_heights = temp_new_heights



    return total_removed, new_heights
