def insert_song(pl, song):
    pl.append(song)
    i = len(pl) - 2
    while i >= 0 and pl[i][1] > song[1]:
        pl[i + 1] = pl[i]
        i -= 1
    pl[i + 1] = song
    return pl

playlist = [("Intro",120), ("Chill Beat",210), ("Long Jam",340)]
print(insert_song(playlist, ("Quick Track",180)))