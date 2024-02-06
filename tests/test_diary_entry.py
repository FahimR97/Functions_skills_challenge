from lib.Diary_entry import *

def test_for_blank_initialisation():
    diary_entry = DiaryEntry("","")
    assert diary_entry.title or diary_entry.contents == ""

def test_add_a_title():
    diary_entry = DiaryEntry("Hello world","")
    assert diary_entry.title == "Hello world"

def test_add_some_contents():
    diary_entry = DiaryEntry("","These are the contents")
    assert diary_entry.contents == "These are the contents"

def test_using_the_format():
    diary_entry = DiaryEntry("Hello world","These are the contents")
    result = diary_entry.format()
    assert result == "Hello world, These are the contents"

def test_counting_the_words():
    diary_entry = DiaryEntry("Hello world","These are the contents")
    formatted = diary_entry.count_words()
    assert formatted == 6


def test_for_reading():
    diary_entry = DiaryEntry("Monday", "Serendipity leads to quixotic, ephemeral moments, crafting an ineffable tapestry. Nebulous thoughts create a quagmire, and verbose conversations obfuscate understanding. Pernicious circumstances reveal esoteric complexities, with disparate perspectives emerging. Amidst evanescent existence, an enigmatic beauty arises, juxtaposing ostentatious displays with humble paragons. Embrace the serendipity weaving life's fabric cheese sneeze.")
    result = diary_entry.reading_time(50)
    assert result == "Your reading time is 1.0 min(s)"

