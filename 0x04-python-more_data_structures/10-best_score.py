#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return (None)
    best = max(list(sorted(a_dictionary.values())))
    for key in a_dictionary:
        if best == a_dictionary[key]:
            return (key)
    return (None)
