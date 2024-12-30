def dice_throws(number, faces, total):
    if total < number or total > faces * number:
        return 0

    return next_dice(0, faces, total, number)


def next_dice(temp_count, faces, total, number):
    if number == 0:
        if temp_count == total:
            return 1
        else:
            return 0
    count = 0
    for i in range(1, faces+1):
        if temp_count + i <= total:
            count += next_dice(temp_count + i, faces, total, number - 1)
    return count