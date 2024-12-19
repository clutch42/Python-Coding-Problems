from collections import deque

def merge_lists(playlists):
    songs = {}
    distinct = set()
    for list in playlists:
        for i in range(len(list)):
            distinct.add(list[i])
            if i < len(list)-1:
                if list[i] not in songs:
                    songs[list[i]] = set()
                songs[list[i]].add(list[i+1])

    dependencies = {song: 0 for song in distinct}

    for list in playlists:
        for i in range(1, len(list)):
            dependencies[list[i]] += 1


    new_playlist = []
    temp = deque([song for song in dependencies if dependencies[song] == 0])
    # processed = set()

    while temp:
        song = temp.popleft()  # Use deque's popleft() for O(1) time complexity
        new_playlist.append(song)
        # processed.add(song)

        # Decrease indegree of dependent songs and add them to temp if their indegree becomes 0
        for value in dependencies:
            if value

    # Check if there's a cycle (i.e., not all songs have been processed)
    # Corrected cycle detection: Check if any songs have non-zero indegree
    if any(dependencies[song] > 0 for song in dependencies):
        print("There is a cycle in the song dependencies!")
        return []

    return new_playlist
