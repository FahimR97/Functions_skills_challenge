#a function called count_words that takes a string as an argument and returns the number of words in the string

def count_words(string):
    words = string.split()
    return len(words)