from lib.music_library import MusicLibrary
from lib.track import Track

"""
Given I add two tracks
I can see them represented in the list
"""

def test_adds_multiple_tracks_and_lists_them():
    library = MusicLibrary()
    track_1 = Track("21 Questions", "50 Cent")
    track_2 = Track("99 Problems", "Jay Z")
    library.add(track_1)
    library.add(track_2)
    assert library.all() == [track_1,track_2]

"""
Given I add two tracks, if I search for 
the name of one of the tracks, I should be able
I get that track back in the results
"""

def test_searches_by_title():
    library = MusicLibrary()
    track_1 = Track("21 Questions", "50 Cent")
    track_2 = Track("99 Problems", "Jay Z")
    library.add(track_1)
    library.add(track_2)
    assert library.search_by_title("21 Questions") == [track_1]

def test_searches_by_part_of_title():
    library = MusicLibrary()
    track_1 = Track("21 Questions", "50 Cent")
    track_2 = Track("99 Problems", "Jay Z")
    library.add(track_1)
    library.add(track_2)
    assert library.search_by_title("21") == [track_1]