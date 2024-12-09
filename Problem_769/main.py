# Alice wants to join her school's Probability Student Club. Membership dues are computed via one of two simple probabilistic games.

# The first game: roll a die repeatedly. Stop rolling once you get a five followed by a six. Your number of rolls is the amount you pay, in dollars.

# The second game: same, except that the stopping condition is a five followed by a five.

# Which of the two games should Alice elect to play? Does it even matter? Write a program to simulate the two games and calculate their expected value.
from roll_dice import number_of_tries

if __name__ == "__main__":
    numbers = []
    while True:
        user_input = input("Enter a number 1 - 6 or x to finish: ")
        if user_input == "x":
            break
        elif user_input == "1":
            numbers.append(1)
        elif user_input == "2":
            numbers.append(2)
        elif user_input == "3":
            numbers.append(3)
        elif user_input == "4":
            numbers.append(4)
        elif user_input == "5":
            numbers.append(5)
        elif user_input == "6":
            numbers.append(6)
    while True:
        user_input = input("Enter number of tries: ")
        try:
            temp = int(user_input)
            if temp > 0:
                test_rolls = temp
                break
            else:
                print("Enter number greater than 0: ", end="")
        except ValueError:
            print("Enter number greater than 0: ", end="")
    for num in numbers:
        print(num, end=" ")
    print()
    averageRolls = number_of_tries(numbers, test_rolls)
    print(f"Average rolls to hit numbers in order from {test_rolls} tries: {averageRolls}")


