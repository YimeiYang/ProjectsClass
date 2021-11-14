# COMP 202 A2 Part 1
# Author: Yimei Yang
# Student ID: 260898303

import doctest
INCOMPLETE = -1

# These constants are for you to use
IRREGULAR_CHARS = " -–`'’«»"
DIGITS = '1234567890'
PUNCTUATION = ',;:.?!"(*)' 

LETTERS = ['abcdefghij', 
           'klmnopqrst', 
           'uvxyzçéàèù',
           'âêîôûëïüœw'] 

################ Functions


def is_in_decade(c, decade):
    '''(str, str) -> bool
    Return whether c is a single-letter character contained within decade.

    >>> is_in_decade('a', 'abcdefghij')
    True
    >>> is_in_decade('z', 'abcdefghij')
    False
    >>> is_in_decade('a', 'âêîôûëïüœw')
    False
    >>> is_in_decade('âêî', 'âêîôûëïüœw')
    False
    '''
    #to see whether any of a character in decade matches with c
    for i in range(len(decade)):
        if(c == decade[i]):
            return True;
        
    return False;


def is_irregular(c):
    '''(str) -> bool
    Return whether character c is a single one of the irregular characters
    in French Braille. Note the global variable we made for you: IRREGULAR_CHARS.

    >>> is_irregular(' ')
    True
    >>> is_irregular('’')
    True
    >>> is_irregular(')')
    False
    >>> is_irregular('-')
    True
    >>> is_irregular('`')
    True
    >>> is_irregular("'")
    True
    >>> is_irregular('a')
    False
    >>> is_irregular('')
    False
    >>> is_irregular('1')
    False
    >>> is_irregular('«»')
    False
    >>> is_irregular('(1-1)')
    False
    '''
    #to check whether the input contains only one character and whether
    #it is a irregular character
    if(len(c) == 1 and c in IRREGULAR_CHARS):
        return True;
        
    return False;


def is_digit(c):
    '''(str) -> bool
    Return whether character c represents a single digit.
    Note the global variable we made for you: DIGITS.

    >>> is_digit('2')
    True
    >>> is_digit('0')
    True
    >>> is_digit('12')
    False
    '''
    #to check whether the input contains only one character and whether
    #it is a digit
    if(len(c) == 1 and c in DIGITS):
        return True;
        
    return False;
    

def is_punctuation(c):
    '''(str) -> bool
    Return whether c is a single character that is one of the common, regular
    forms of punctuation in French Braille.
    Note the global variable we made for you: PUNCTUATION.

    >>> is_punctuation(',')
    True
    >>> is_punctuation(',,')
    False
    >>> is_punctuation('-')
    False
    >>> is_punctuation('"')
    True
    >>> is_punctuation('')
    False
    >>> is_punctuation('a')
    False
    '''
    #to check whether the input contains only one character and whether
    #it is a punctuation
    if(len(c) == 1 and c in PUNCTUATION):
        return True;

    return False;

def is_letter(c):
    '''(str) -> bool
    Return whether c is a single one of one of the standard letters
    in French Braille. Provided to students.
    Do not edit this function.

    >>> is_letter('a')
    True
    >>> is_letter('z')
    True
    >>> is_letter('w')
    True
    >>> is_letter('é')
    True
    >>> is_letter('A')
    True
    >>> is_letter('Œ')
    True
    >>> is_letter('1')
    False
    >>> is_letter('ß')
    False
    >>> is_letter('aa')
    False
    >>> is_letter('Hello')
    False
    '''
    c = c.lower()
    for decade in LETTERS:
        if is_in_decade(c, decade):
            return True
    return False


def is_known_character(c):
    '''(str) -> bool
    Is c one of the characters supported by French Braille?
    (Letter, digit, punctuation or irregular.)

    >>> is_known_character('a')
    True
    >>> is_known_character('É')
    True
    >>> is_known_character('-')
    True
    >>> is_known_character('4')
    True
    >>> is_known_character('.')
    True
    >>> is_known_character('@')
    False
    >>> is_known_character('ß')
    False
    >>> is_known_character('\\n')
    False
    '''
    #to check whether c is either a irregular character, digit, punctuation, or
    #letter.
    return (is_irregular(c) or is_digit(c) \
            or is_punctuation(c) or is_letter(c));


def is_capitalized(c):
    '''(str) -> bool
    Return whether c is a single capitalized letter supported by French Braille.

    >>> is_capitalized('A') 
    True
    >>> is_capitalized('a')
    False
    >>> is_capitalized('W')
    True
    >>> is_capitalized('É')
    True
    >>> is_capitalized(' ')
    False
    >>> is_capitalized('')
    False
    >>> is_capitalized('Δ')
    False
    >>> is_capitalized('femmes')
    False
    >>> is_capitalized('FEMMES')
    False
    '''
    #to check whether c contains only one character and whether it is a letter.
    if (len(c) == 1 and is_letter(c)):
       if(c != c.lower()):
           return True; 
    return False;


#########################################

if __name__ == '__main__':
    doctest.testmod()
