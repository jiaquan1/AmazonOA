def favgenres(usersongs,songgenres):
    output = {}
    d_song = {}
    for genre in songgenres:
        for song in songgenres[genre]:
            d_song[song]=genre
    for user in usersongs:
        songlist = usersongs[user]
        count = {}
        for song in songlist:
            genre=d_song[song]
            count[genre] = count.get(genre,0)+1
        output[user]=[key for key, val in count.items() if val == max(count.values())]
    return output

userSongs = {  
       "David": ["song1", "song2", "song3", "song4", "song8"],
       "Emma":  ["song5", "song6", "song7"]
    }
songGenres = {  
       "Rock":    ["song1", "song3"],
       "Dubstep": ["song7"],
       "Techno":  ["song2", "song4"],
       "Pop":     ["song5", "song6"],
       "Jazz":    ["song8", "song9"]
    }
print(favgenres(userSongs,songGenres)) 



