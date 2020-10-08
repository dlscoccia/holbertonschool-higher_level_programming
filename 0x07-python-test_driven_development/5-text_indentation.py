#!/usr/bin/python3
''' Module '''


def text_indentation(text):
    ''' indentation tool '''
    symbol = ['.', '?', ':']
    indented_text = ""

    if type(text) is str:
        for i in text:
            indented_text = indented_text + i
            if i in symbol:
                print(indented_text.strip())
                print("")
                indented_text = ""
        print(indented_text.strip(), end="")
    else:
        raise TypeError("text must be a string")
