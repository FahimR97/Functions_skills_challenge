class Music_tracker:

    def __init__(self):
        # blank list to hold the music
        self.list = []


    def add_music(self,track):
        #function to add tracks, appends to list
        songs = self.list.append(track)
        return songs

    def see_tracks(self):
        #Function which shows current tracks in list
        return self.list