from lib.track_music_listening import *




#Test to view empty list
def test_view_empty_list():
    view_list = Music_tracker()
    assert view_list.see_tracks() == []

#Test to add one track
#Test to see the current list 
    
def test_add_one_track():
    music_list = Music_tracker()
    music_list.add_music("Candy shop")
    assert music_list.see_tracks() == ["Candy shop"]

#Test to add multiple tracks

def test_add_multiple_individually():
    music_list = Music_tracker()
    music_list.add_music("Candy shop")
    music_list.add_music("21 Seconds")
    assert music_list.see_tracks() == ["Candy shop","21 Seconds"]



def test_add_multiple_together():
    music_list = Music_tracker()
    music_list.add_music(["Candy shop","21 Seconds"])
    assert music_list.see_tracks() == [["Candy shop","21 Seconds"]]


