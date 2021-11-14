# COMP 202 A2 Part 5
# Author: Yimei Yang
# Student ID: 260898303
from text_to_braille import *

ENG_CAPITAL = '..\n..\n.o'
NUMBER = '.o\n.o\noo'
ENG_NUM_END = '..\n.o\n.o'
# You may want to define more global variables here

####################################################
# Here are two helper functions to help you get started

def two_letter_contractions(text):
    '''(str) -> str
    Process English text so that the two-letter contractions are changed
    to the appropriate French accented letter, so that when this is run
    through the French Braille translator we get English Braille.
    Provided to students. You should not edit it.

    >>> two_letter_contractions('chat')
    'âat'
    >>> two_letter_contractions('shed')
    'îë'
    >>> two_letter_contractions('shied')
    'îië'
    >>> two_letter_contractions('showed the neighbourhood where')
    'îœë ôe neiêbürhood ûïe'
    >>> two_letter_contractions('SHED')
    'ÎË'
    >>> two_letter_contractions('ShOwEd tHE NEIGHBOURHOOD Where') 
    'ÎŒË tHE NEIÊBÜRHOOD Ûïe'
    '''
    combos = ['ch', 'gh', 'sh', 'th', 'wh', 'ed', 'er', 'ou', 'ow']
    for i, c in enumerate(combos):
        text = text.replace(c, LETTERS[-1][i])
    for i, c in enumerate(combos):
        text = text.replace(c.upper(), LETTERS[-1][i].upper())
    for i, c in enumerate(combos):
        text = text.replace(c.capitalize(), LETTERS[-1][i].upper())

    return text


def whole_word_contractions(text):
    '''(str) -> str
    Process English text so that the full-word contractions are changed
    to the appropriate French accented letter, so that when this is run
    through the French Braille translator we get English Braille.

    If the full-word contraction appears within a word, 
    contract it. (e.g. 'and' in 'sand')

    Provided to students. You should not edit this function.

    >>> whole_word_contractions('with')
    'ù'
    >>> whole_word_contractions('for the cat with the purr and the meow')
    'é à cat ù à purr ç à meow'
    >>> whole_word_contractions('With')
    'Ù'
    >>> whole_word_contractions('WITH')
    'Ù'
    >>> whole_word_contractions('wiTH')
    'wiTH'
    >>> whole_word_contractions('FOR thE Cat WITh THE purr And The meow')
    'É thE Cat WITh À purr Ç À meow'
    >>> whole_word_contractions('aforewith parenthetical sand')
    'aéeù parenàtical sç'
    >>> whole_word_contractions('wither')
    'ùer'
    '''
    # putting 'with' first so wither becomes with-er not wi-the-r
    words = ['with', 'and', 'for', 'the']
    fr_equivs = ['ù', 'ç', 'é', 'à', ]
    # lower case
    for i, w in enumerate(words):
        text = text.replace(w, fr_equivs[i])
    for i, w in enumerate(words):
        text = text.replace(w.upper(), fr_equivs[i].upper())
    for i, w in enumerate(words):
        text = text.replace(w.capitalize(), fr_equivs[i].upper())
    return text



####################################################
# These two incomplete helper functions are to help you get started

def convert_contractions(text):
    '''(str) -> str
    Convert English text so that both whole-word contractions
    and two-letter contractions are changed to the appropriate
    French accented letter, so that when this is run
    through the French Braille translator we get English Braille.

    Refer to the docstrings for whole_word_contractions and 
    two_letter_contractions for more info.

    >>> convert_contractions('with')
    'ù'
    >>> convert_contractions('for the cat with the purr and the meow')
    'é à cat ù à purr ç à meœ'
    >>> convert_contractions('chat')
    'âat'
    >>> convert_contractions('wither')
    'ùï'
    >>> convert_contractions('aforewith parenthetical sand')
    'aéeù parenàtical sç'
    >>> convert_contractions('Showed The Neighbourhood Where')
    'Îœë À Neiêbürhood Ûïe'
    '''
    # ADD CODE HERE
    #convert the whole-word contractions
    Word_c = whole_word_contractions(text)
    #convert the two letter contractions
    result = two_letter_contractions(Word_c)
    return result


def convert_quotes(text):
    '''(str) -> str
    Convert the straight quotation mark into open/close quotations.
    >>> convert_quotes('"Hello"')
    '“Hello”'
    >>> convert_quotes('"Hi" and "Hello"')
    '“Hi” and “Hello”'
    >>> convert_quotes('"')
    '“'
    >>> convert_quotes('"""')
    '“”“'
    >>> convert_quotes('" "o" "i" "')
    '“ ”o“ ”i“ ”'
    '''
    # ADD CODE HERE
    count = 0
    #creat a new string to store the changed content
    New_text = ""
    #loop though every element in the input
    for i in range(len(text)):
        #change " to “ if it is the number of " that can be divided by 2 and
        #vice versa
        if(text[i] == '"'):
            if(count % 2 ==0):
                New_text = New_text + '“'
                count = count + 1
            else:
                New_text = New_text + '”'
                count = count + 1
        else:
            New_text = New_text + text[i]
    return New_text 


####################################################
# Put your own helper functions here!
def French_Beg_End(french_input):
    '''(str)->str
    Add the beginning unicode and the ending unicode to numbers in the input
    >>> French_Beg_End("COMP 250")
    'COMP ⠼250⠰'
    >>> French_Beg_End("COMP 202")
    'COMP ⠼202⠰'
    >>> French_Beg_End("123")
    '⠼123⠰'
    >>> French_Beg_End("COMP")
    'COMP'
    >>> French_Beg_End("COMP 2 COMP")
    'COMP ⠼2⠰ COMP'
    >>> French_Beg_End("COMP 202 COMP 250")
    'COMP ⠼202⠰ COMP ⠼250⠰'
    >>> French_Beg_End("2")
    '⠼2⠰'
    '''
    #creat a new string to store the changed content
    New_line = ""
    #loop though every element in the input
    for i in range(len(french_input)):
        #check if it is a digit
        if (is_digit(french_input[i])):
            #if the digit is not at the first nor the last index of the input  
            if (i!=0 and i!=len(french_input)-1):
                #if the element before the digit and the one after is are both
                #not digit
                if(not is_digit(french_input[i+1]) and \
                   not is_digit(french_input[i-1])):
                    #add both the beginning and the ending unicode to the digit
                    New_line = New_line + ostring_to_unicode(NUMBER)\
                               + french_input[i] + \
                               ostring_to_unicode(ENG_NUM_END)
                #if only the element after the digit is not digit
                elif(not is_digit(french_input[i+1])):
                    #add the ending unicode to the digit
                    New_line = New_line + french_input[i] + \
                               ostring_to_unicode(ENG_NUM_END)
                #if only the element after the digit is not digit
                elif(not is_digit(french_input[i-1])):
                    #add the beginning unicode to the digit
                    New_line = New_line + ostring_to_unicode(NUMBER) + \
                               french_input[i]
                #if the element before the digit and the one after is are both
                # digits
                elif(is_digit(french_input[i])):
                    #add the digit to the new string
                    New_line = New_line + french_input[i]
            #if the digit is not at the first but the last index of the input 
            elif(i!= 0 and i == len(french_input)-1):
                #add the ending unicode to the digit
                New_line = New_line + french_input[i]+\
                           ostring_to_unicode(ENG_NUM_END)
            #if the digit is at the first index of the input
            elif(i == 0):
                #if the digit is at the first and the last index of the input
                if(len(french_input) == 1):
                    #add both the beginning and the ending unicode to the digit
                    New_line = New_line + \
                               ostring_to_unicode(NUMBER)+ \
                               french_input[i] + ostring_to_unicode(ENG_NUM_END)
                #if the digit is only at the first index of the input
                else:
                    #add the beginning unicode to the digit
                    New_line = New_line + \
                               ostring_to_unicode(NUMBER)+ french_input[i]
        else:
            New_line = New_line + french_input[i]
    return New_line

def Num_to_letter(input_with_braille):
    '''
    (str)->str
    Convert numbers to their corresponding alphabets
    >>> Num_to_letter("COMP ⠼250⠰")
    'COMP ⠼bej⠰'
    >>> Num_to_letter("COMP ⠼202⠰")
    'COMP ⠼bjb⠰'
    >>> Num_to_letter('⠼2⠰')
    '⠼b⠰'
    >>> Num_to_letter("123")
    'abc'
    >>> Num_to_letter("COMP")
    'COMP'
    '''
    New_line2 = ""
    for i in range(len(input_with_braille)):
        #check whether each character in the input is a digit
        if(is_digit(input_with_braille[i])):
            #Convert numbers to their corresponding alphabets
            if(input_with_braille[i] == "1"):
                New_line2 = New_line2 + "a"
            elif(input_with_braille[i] == "2"):
                New_line2 = New_line2 + "b"
            elif(input_with_braille[i] == "3"):
                New_line2 = New_line2 + "c"
            elif(input_with_braille[i] == "4"):
                New_line2 = New_line2 + "d"
            elif(input_with_braille[i] == "5"):
                New_line2 = New_line2 + "e"
            elif(input_with_braille[i] == "6"):
                New_line2 = New_line2 + "f"
            elif(input_with_braille[i] == "7"):
                New_line2 = New_line2 + "g"
            elif(input_with_braille[i] == "8"):
                New_line2 = New_line2 + "h"
            elif(input_with_braille[i] == "9"):
                New_line2 = New_line2 + "i"
            elif(input_with_braille[i] == "0"):
                New_line2 = New_line2 + "j"
        else:
            New_line2 = New_line2 + input_with_braille[i]
    return New_line2
            
def questionMark_change(unicode):
    '''
    Convert English question mark unicode to French question mark unicode
    >>> questionMark_change("⠠⠿ ⠩⠁⠏⠑⠎ ⠾ ⠉⠕⠇⠳⠗⠢")
    '⠠⠿ ⠩⠁⠏⠑⠎ ⠾ ⠉⠕⠇⠳⠗⠦'
    >>> questionMark_change("⠠⠑⠎ ⠾ ⠉⠕⠇⠳⠗⠢")
    '⠠⠑⠎ ⠾ ⠉⠕⠇⠳⠗⠦'
    >>> questionMark_change("⠠⠿ ⠩⠁⠏⠑⠎ ⠾ ⠇⠳⠗⠢")
    '⠠⠿ ⠩⠁⠏⠑⠎ ⠾ ⠇⠳⠗⠦'
    '''
    New_line = ""
    #convert every ⠢ to ⠦
    for i in range(len(unicode)):
        if(unicode[i] == "⠢"):
            New_line = New_line + '⠦'
        else:
            New_line = New_line + unicode[i]
    return New_line

def parentheses_change(unicode):
    '''
    (str)->str
    Convert English parentheses mark unicode to French parentheses mark unicode
    >>> parentheses_change('⠦⠓⠊⠴')
    '⠶⠓⠊⠶'
    >>> parentheses_change('⠦⠠⠏⠁⠗⠑⠝⠷⠞⠊⠉⠁⠇⠴')
    '⠶⠠⠏⠁⠗⠑⠝⠷⠞⠊⠉⠁⠇⠶'
    >>> parentheses_change('⠦⠏⠓⠕⠝⠕⠛⠗⠁⠍⠎⠴')
    '⠶⠏⠓⠕⠝⠕⠛⠗⠁⠍⠎⠶'
    '''
    parenUni = ""
    for i in range(len(unicode)):
        #convert every ⠦ and ⠴ to ⠶
        if(unicode[i] == '⠦' or unicode[i] == '⠴'):
            parenUni = parenUni + '⠶'
        else:
            parenUni = parenUni + unicode[i]
    return parenUni 
def quotationMarks_change(unicode):
    '''
    Convert English quotation mark unicode to French quotation mark unicode
    >>> quotationMarks_change('“⠠⠟⠥⠕⠞⠁⠞⠊⠕⠝”')
    '⠦⠠⠟⠥⠕⠞⠁⠞⠊⠕⠝⠴'
    >>> quotationMarks_change('“⠓⠊”')
    '⠦⠓⠊⠴'
    >>> quotationMarks_change('“⠠⠩⠳⠞⠂')
    '⠦⠠⠩⠳⠞⠂'
    '''
    quotaUni = ""
    for i in range(len(unicode)):
        #convert “ to ⠦ and ” to ⠴
        if(unicode[i] == '“'):
            quotaUni = quotaUni + '⠦'
        elif(unicode[i] == '”'):
            quotaUni = quotaUni + '⠴'
        else:
            quotaUni = quotaUni + unicode[i]
    return quotaUni 
    


####################################################

def english_text_to_braille(text):
    '''(str) -> str
    Convert text to English Braille. Text could contain new lines.

    This is a big problem, so think through how you will break it up
    into smaller parts and helper functions.
    Hints:
        - you'll want to call text_to_braille
        - you can alter the text that goes into text_to_braille
        - you can alter the text that comes out of text_to_braille
        - you shouldn't have to manually enter the Braille for 'and', 'ch', etc

    You are expected to write helper functions for this, and provide
    docstrings for them with comprehensive tests.

    >>> english_text_to_braille('202') # numbers
    '⠼⠃⠚⠃⠰'
    >>> english_text_to_braille('2') # single digit
    '⠼⠃⠰'
    >>> english_text_to_braille('COMP') # all caps
    '⠠⠠⠉⠕⠍⠏'
    >>> english_text_to_braille('COMP 202') # combining number + all caps
    '⠠⠠⠉⠕⠍⠏ ⠼⠃⠚⠃⠰'
    >>> english_text_to_braille('and')
    '⠯'
    >>> english_text_to_braille('and And AND aNd')
    '⠯ ⠠⠯ ⠠⠯ ⠁⠠⠝⠙'
    >>> english_text_to_braille('chat that the with')
    '⠡⠁⠞ ⠹⠁⠞ ⠷ ⠾'
    >>> english_text_to_braille('hi?')
    '⠓⠊⠦'
    >>> english_text_to_braille('(hi)')
    '⠶⠓⠊⠶'
    >>> english_text_to_braille('"hi"')
    '⠦⠓⠊⠴'
    >>> english_text_to_braille('COMP 202 AND COMP 250')
    '⠠⠠⠉⠕⠍⠏ ⠼⠃⠚⠃⠰ ⠠⠯ ⠠⠠⠉⠕⠍⠏ ⠼⠃⠑⠚⠰'
    >>> english_text_to_braille('For shapes with colour?')
    '⠠⠿ ⠩⠁⠏⠑⠎ ⠾ ⠉⠕⠇⠳⠗⠦'
    >>> english_text_to_braille('(Parenthetical)\\n\\n"Quotation"')
    '⠶⠠⠏⠁⠗⠑⠝⠷⠞⠊⠉⠁⠇⠶\\n\\n⠦⠠⠟⠥⠕⠞⠁⠞⠊⠕⠝⠴'
    '''
    # You may want to put code after this comment. You can also delete this comment.
    # Here's a line we're giving you to get started: change text so the
    # contractions become the French accented letter that they correspond to
    text = convert_contractions(text)
    #Add the beginning unicode and the ending unicode to numbers in the input
    text = French_Beg_End(text)
    #Convert numbers to their corresponding alphabets
    text = Num_to_letter(text)
    #Convert the straight quotation mark into open/close quotations.
    text = convert_quotes(text)
    # Run the text through the French Braille translator
    text = text_to_braille(text)
    #Convert English parentheses mark unicode to French parentheses mark unicode
    text = parentheses_change(text)
    #Convert English quotation mark unicode to French quotation mark unicode
    text = quotationMarks_change(text)
    #Convert English question mark unicode to French question mark unicode
    text = questionMark_change(text)
    # Replace the French capital with the English capital
    text = text.replace(ostring_to_unicode(CAPITAL), ostring_to_unicode('..\n..\n.o'))
    return text

def english_file_to_braille(fname):
    '''(str) -> NoneType
    Given English text in a file with name fname in folder tests/,
    convert it into English Braille in Unicode.
    Save the result to fname + "_eng_braille".
    Provided to students. You shouldn't edit this function.

    >>> english_file_to_braille('test4.txt')
    >>> file_diff('tests/test4_eng_braille.txt', 'tests/expected4.txt')
    True
    >>> english_file_to_braille('test5.txt')
    >>> file_diff('tests/test5_eng_braille.txt', 'tests/expected5.txt')
    True
    >>> english_file_to_braille('test6.txt')
    >>> file_diff('tests/test6_eng_braille.txt', 'tests/expected6.txt')
    True
    '''  
    file_to_braille(fname, english_text_to_braille, "eng_braille")


if __name__ == '__main__':
    doctest.testmod()    # you may want to comment/uncomment along the way
    # and add tests down here
