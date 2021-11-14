# COMP 202 A4 Part 2
# Name:Yimei Yang
# Student ID: 260898303
import datetime
import numpy as np
import matplotlib.pyplot as plt
import doctest
from datetime import date

def date_diff(first_time, second_time):
    '''
    >>> date_diff('2018-10-31', '2019-11-2')
    367
    >>> date_diff('2019-11-2', '2019-10-31')
    -2
    >>> date_diff('2019-9-1', '2019-10-20')
    49
    '''
    #get the year, month, day strings from 2 inputs
    first_year = first_time[0:4]
    if(first_time[6:7] == "-"):
        first_month = first_time[5:6]
    else:
        first_month = first_time[5:7]
    if(first_time[6:7] == "-"):
        first_day = first_time[7:]
    else:
        first_day = first_time[8:]
    second_year = second_time[0:4]
    if(second_time[6:7] == "-"):
        second_month = second_time[5:6]
    else:
        second_month = second_time[5:7]
    if(second_time[6:7] == "-"):
        second_day = second_time[7:]
    else:
        second_day = second_time[8:]
    #convert the num to the datetime 
    first_date = datetime.date(int(first_year), int(first_month), int(first_day))
    second_date = datetime.date(int(second_year), int(second_month), int(second_day))
    #get the difference
    diff = first_date - second_date
    #reverse the result
    num_diff = - diff.days
    return num_diff


def get_age(first_time, second_time):
    '''
    >>> get_age('2018-10-31', '2019-11-2')
    1
    >>> get_age('2018-10-31', '2000-11-2')
    -17
    '''
    #get the diff date
    day_diff = date_diff(first_time, second_time)
    #devide it by 365.2425 to get the diff year
    year_diff = int(day_diff/365.2425)
    return year_diff

def stage_three(input_filename, output_filename):
    '''
    >>> stage_three('stage2.txt', 'stage3.txt')
    {'0': {'I': 1, 'R': 0, 'M': 0}, '1': {'I': 3, 'R': 0, 'M': 0}, '2': {'I': 8, 'R': 0, 'M': 0}, '3': {'I': 21, 'R': 0, 'M': 0}, '4': {'I': 50, 'R': 1, 'M': 2}, '5': {'I': 106, 'R': 0, 'M': 25}, '6': {'I': 278, 'R': 6, 'M': 25}, '7': {'I': 740, 'R': 1, 'M': 47}, '8': {'I': 1586, 'R': 13, 'M': 87}}
    '''

    first_line_s = []
    B_dict = {}
    count = 4
    input_file = open(input_filename, 'r')
    output_file = open(output_filename, 'w+', encoding = 'utf-8')
    #read the first line of the file to get the index date
    first_line = input_file.readline()
    input_file.seek(0)
    first_line_s = first_line.split("\t")
    index_date = first_line_s[2]
    #loop through every line of the file to get the date
    #and brith and make them compare to the index date
    for line in input_file:
        line_s = []
        line_s = line.split("\t")
        date_time = line_s[2]
        birth_time = line_s[3]
        diff_date = date_diff(index_date, date_time)
        diff_birth = get_age(birth_time, index_date)
        line = line.replace(birth_time, str(diff_birth))
        line = line.replace(date_time, str(diff_date))
        state = line_s[6]
        #change all the stage to I, R, or M
        if(state[0:1] == "I" or state[0:1] == "i"):
            line = line.replace(state, "I")     
        elif(state[0:1] == "r" or state[0:1] == "R"):
            line = line.replace(state, "R")
        elif(state[0:1] == "m" or state[0:1] == "M" \
             or state[0:1] == "D" or state[0:1] == "d"):
            line = line.replace(state, "M")
        output_file.write(line)
    output_file.seek(0)
    #set all the days of pandemic as keys
    for line in output_file:
        line_s_2 = []
        line_s_2 = line.split("\t")
        keyB = line_s_2[2]
        B_dict[keyB] = {"I":0, "R":0, "M":0}
    output_file.seek(0)
    #put numers of I, R, or M in to the dictionary to their corresponding keys
    for line in output_file:
        line_s_3 = []
        line_s_3 = line.split("\t")
        keyB = line_s_3[2]
        keyS = line_s_3[6]
        B_dict[keyB][keyS] = B_dict[keyB][keyS] + 1
    #return the dictionary
    return B_dict
def plot_time_series(d):
    '''
    >>> d = stage_three('stage2.txt', 'stage3.txt')
    >>> plot_time_series(d)
    [[1, 0, 0], [3, 0, 0], [8, 0, 0], [21, 0, 0], [50, 1, 2], [106, 0, 25], [278, 6, 25], [740, 1, 47], [1586, 13, 87]]
    '''
    new_list = []
    days = len(d)
    double_list = []
    yI = []
    yR = []
    yM = []
    #put numbers of infected, recovered, and dead people \
    #for different days of pandemic into a list
    for keyB in d:
        for keyS in d[keyB]:
            new_list.append(d[keyB][keyS])
    #slice the infected, recovered, and dead people group out and put them into a nested list
    i = 0
    while i < len(new_list):
        double_list.append(new_list[i:i+3])
        i+=3
    #set the x-axis to be days into pandemic
    x = np.arange(days)
    #set the y-axis of infected people to be the first element in each I, R, M group
    #set the y-axis of recoverd people to be the second element in each I, R, M group
    #set the y-axis of dead people to be the third element in each I, R, M group
    for group in double_list:
        yI.append(group[0])
        yR.append(group[1])
        yM.append(group[2])
    np_yI = np.array(yI)
    np_yR = np.array(yR)
    np_yM = np.array(yM)
    #draw the graph
    plt.plot(x, np_yI, "b")
    plt.plot(x, np_yR, 'g')
    plt.plot(x, np_yM, "c")
    plt.title("Time series of early pandemic, by Yimei Yang")
    plt.xlabel('Days into Pandemic')
    plt.ylabel("Number of People")
    plt.legend(['Infected', 'Recovered', 'Dead'])

    plt.savefig("time_series.png")
    #return the nested list
    return double_list
if __name__ == '__main__':
    doctest.testmod()
