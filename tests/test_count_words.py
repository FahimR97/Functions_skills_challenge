from lib.count_words import *

#Check for a blank string 

def test_for_blank_string():
    result = count_words("")
    assert result == 0

def test_two_words():
    result = count_words("Hello Fahim")
    assert result == 2
