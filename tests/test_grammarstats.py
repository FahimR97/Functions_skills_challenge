from lib.grammarstats import *

def test_the_check():
    grammar = GrammarStats()
    result = grammar.check("Hello!")
    assert result == True

def test_check_one_false():
    grammar = GrammarStats()
    grammar.check("hello")
    result = grammar.percentage_good()
    assert result == 0

def test_for_50_percent():
    grammar = GrammarStats()
    grammar.check("hello")
    grammar.check("Hello!")
    result = grammar.percentage_good()
    assert result == 50

def test_for_100_percent():
    grammar = GrammarStats()
    grammar.check("Hello!")
    grammar.check("World?")
    result = grammar.percentage_good()
    assert result == 100
    