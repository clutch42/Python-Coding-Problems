def find_rooms(times):
    if len(times) == 0:
        return 0
    start_times = sorted([time[0] for time in times])
    end_times = sorted([time[1] for time in times])
    print(start_times)
    print(end_times)
    max_rooms = 0
    current_rooms = 0
    start_index = end_index = 0
    while start_index < len(start_times):
        if start_times[start_index] < end_times[end_index]:
            current_rooms += 1
            start_index += 1
        else:
            current_rooms -= 1
            end_index += 1
        max_rooms = max(max_rooms, current_rooms)
    return max_rooms
