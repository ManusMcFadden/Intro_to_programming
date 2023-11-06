# -*- coding: utf-8 -*-

def string_to_morse_code(x):
    """
    Returns the morse code of a string x.
    If x is not a string, returns 'ValueError, string expected!'.
    """

    mcode = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
             'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
             'K': '-.-', 'L': '.-..', 'M': '--',   'N': '-.', 'O': '---',
             'P': '.--.', 'Q': '--.-', 'R': '.-.',  'S': '...', 'T': '-',
             'U': '..-', 'V': '...-', 'W': '.--',  'X': '-..-', 'Y': '-.--',
             'Z': '--..', ' ': ' ', '0': '-----', '1': '.----', '2': '..---',
             '3': '...--', '4': '....-',  '5': '.....',  '6': '-....',
             '7': '--...', '8': '---..',  '9': '----.',  '&': '.-...',
             "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
             ':': '---...', ',': '--..--', '=': '-...-',  '!': '-.-.--',
             '.': '.-.-.-', '-': '-....-', '+': '.-.-.',  '"': '.-..-.',
             '?': '..--..', '/': '-..-.'}

    if not isinstance(x, str):
        return "ValueError, string expected!"
    
    outputstring = ""
    my_list = list(x)
    for c in my_list:
        outputstring += mcode[c]

    return outputstring

print(string_to_morse_code("HELLO"))