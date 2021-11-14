# COMP 202 A4 Part 1
# Name:Yimei Yang
# Student ID: 260898303

import doctest

def which_delimiter(string):
    '''
    (string)-->string
    return the most commonly used delimiter in the input string
    >>> which_delimiter('0 1 2,3\\t4')
    ' '
    >>> which_delimiter('123')
    Traceback (most recent call last):
    AssertionError: Should have at least one delimiter
    >>> which_delimiter("1\\t2\\t3\\t4")
    '\\t'
    >>> which_delimiter("1,2,3")
    ','
    >>> which_delimiter("3\\t0\\t2020/11/29\\t2002/6/1\\tHOMME\\tH4A 2P6\\tINFECTÉ\\t99,8\\t3")
    '\\t'
    '''
    #count the numbers of space, tab, and find the maximum number
    count_s = 0
    count_t = 0
    count_c = 0
    Max_num = 0
    count_s = string.count(" ")
    count_t = string.count("\t")
    count_c = string.count(",")

    Max_num = max(count_s, count_t, count_c)
    #return the character with the maximum number counted

    if(count_t == Max_num and count_t != 0):
        return "\t"
    elif(count_s == Max_num and count_s != 0):
        return " "
    elif(count_c == Max_num and count_c != 0):
        return ","
    elif(count_s == count_t == count_c == 0):
        raise AssertionError("Should have at least one delimiter")
    

def stage_one(input_filename, output_filename):
    '''
    >>> stage_one('260898303.txt', 'stage1.txt')
    3000
    '''
    string = ""
    count = 0
    input_file = open(input_filename, 'r')
    output_file = open(output_filename, 'w', encoding = 'utf-8')
    #loop through every line in the file and change the most
    #common delimiter
    for line in input_file:
        count = count + 1
        common_delimiter = which_delimiter(line)
        if(common_delimiter != "\t"):
            line = line.replace(common_delimiter, "\t")
        else:
            line = line
        #make all alphabet to be uppercased
        line = line.upper()
        line_list = line.split()
        #change the /. in the date to be -
        if len(line_list)!= 0:
            for char in line_list[2]:
                if(char == "/" or char == "."):
                    line_list[2] = line_list[2].replace(char, "-")
            for char in line_list[3]:
                if(char == "/" or char == "."):
                    line_list[3] = line_list[3].replace(char, "-")
            line = "\t".join(line_list)
            output_file.write(line + "\n")
    #return the numbers of lines in the output file
    return count


def stage_two(input_filename, output_filename):
    '''
    >>> stage_two('stage1.txt', 'stage2.txt')
    3000
    '''
    string = ""
    count = 0
    count_t = 0
    list_t = []
    input_file = open(input_filename, 'r')
    output_file = open(output_filename, 'w', encoding = 'utf-8')
    #loop through every line in the input file
    for line in input_file:
        count = count + 1
        #check whether there are 9 column 
        if(line.count("\t") != 8):
            #if there is a C, cut it
            index_c = line.find("\tC")
            if(index_c != -1):
                line = line.replace("\tC", "C")
            #if the temperature is not valid, cut the whitespace
            line = line.replace("NON\tAPPLICABLE", "NONAPPLICABLE")
            #check whether there are 9 colums
            if(line.count("\t") != 8):
                #find the index of the tab within the postal code
                list_t = [i for i, element in enumerate(line) if element == "\t"]
                index_t = list_t[5]
                #eliminate the tab
                parta = line[0:index_t-1]
                partb = line[index_t-1:index_t+1]
                partc = line[index_t+1:]
                partb = partb.replace("\t", "")
                line = parta + partb + partc                       
        output_file.write(line)
    #return the numbers of lines in the output file
    return count


            
                        
            



    
    
    

if __name__ == '__main__':
    doctest.testmod()
