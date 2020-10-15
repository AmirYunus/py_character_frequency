#!/usr/bin/env python3

def character_frequency(filename):
    """
    Counts the frequency of each character in the given file.
    """
    try:
        f = open(filename)

    except OSError:
        return None
    
    characters = {}

    for each_line in f:
        for each_character in each_line:
            characters[each_character] = characters.get(each_character, 0) + 1
    
    f.close()

    return characters