from lib.Diary_entry import *

def test_for_blank_string():
    diary_entry = DiaryEntry("","")
    assert diary_entry.title == ""

def test_add_for_dates():
    diary_entry = DiaryEntry("Tuesday","Hello")
    assert diary_entry.title == "Tuesday"

def test_using_the_formatting():
    diary_entry = DiaryEntry("Dear Diary", "Today I went to the park")
    result = diary_entry.format()
    assert result == "Dear Diary, Today I went to the park"

def test_the_word_counting():
    diary_entry = DiaryEntry("Dear Diary", "Today I went to the park")
    form = diary_entry.format()
    result = form.count_words()
    assert result == 8
