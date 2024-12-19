
def merge_lists(playlists):
    songs = {}
    distinct = set()

    for playlist in playlists:
        for i in range(len(playlist)):
            distinct.add(playlist[i])
            if i < len(playlist)-1:
                if playlist[i] not in songs:
                    songs[playlist[i]] = set()
                songs[playlist[i]].add(playlist[i+1])

    distinct = list(distinct)
    dependencies = [0 for _ in distinct]

    song_index = {song: idx for idx, song in enumerate(distinct)}

    depend_done = set()
    for playlist in playlists:
        for i in range(1, len(playlist)):
            current = (playlist[i-1], playlist[i])
            if current not in depend_done:
                dependencies[song_index[playlist[i]]] += 1
                depend_done.add(current)

    new_playlist = []
    temp = [distinct[i] for i in range(len(distinct)) if dependencies[i] == 0]

    while temp:
        song = temp.pop(0)
        new_playlist.append(song)

        if song in songs:
            for neighbor in songs[song]:
                dependencies[song_index[neighbor]] -= 1
                if dependencies[song_index[neighbor]] == 0 and neighbor not in temp:
                    temp.append(neighbor)

    if len(new_playlist) < len(distinct):
        print("Cycle detected: The playlists have circular dependencies.")
        return []

    return new_playlist
