# Write a function, throw_dice(N, faces, total), that determines how many ways it is possible to throw N dice with some
# number of faces each to get a specific total.
# For example, throw_dice(3, 6, 7) should equal 15.
from Dice_Throws import dice_throws

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    number = input("Enter number of dice: ")
    faces = input("Enter number of faces on dice: ")
    total = input("Enter total of dice: ")
    print(f"The number of combinations with a total of {total} is {dice_throws(int(number), int(faces), int(total))}")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
