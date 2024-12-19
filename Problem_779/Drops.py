def num_of_drops(eggs, floors):
    lowest = 1
    highest = floors
    tries = 0
    while eggs > 1 and lowest < highest:
        mid = (highest + lowest) // 2
        eggs -= 1
        tries += 1
        print(mid)
        print(eggs)
        lower_floors = mid - lowest
        upper_floors = highest - mid
        print(f"lower: {lower_floors}, upper: {upper_floors}")
        if lower_floors > upper_floors:
            highest = mid - 1
        else:
            lowest = mid
    tries += highest - lowest
    return tries
