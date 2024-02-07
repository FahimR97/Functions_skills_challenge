from lib.track import *

def test_construct_track():
    track = Track("99 Problems", "Jay Z")
    assert track.title == "99 Problems"
    assert track.artist == "Jay Z"