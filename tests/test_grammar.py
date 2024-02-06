from lib.grammar import *


def test_no_ending_punctuation():
    result = grammar_check("Hello it is Monday.")
    assert result == True