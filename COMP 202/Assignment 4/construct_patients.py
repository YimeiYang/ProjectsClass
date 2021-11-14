# COMP 202 A4 Part 3
# Name:Yimei Yang
# Student ID: 260898303
import datetime
import numpy as np
import matplotlib.pyplot as plt
import doctest
from datetime import date
NUM = "1234567890"
LET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
class Patient:
    def __init__(self, num, day_diagnosed, age, sex_gender, postal, state, temps,\
                 days_symptomatic):
        list_temps = []
        #initialize num of the patient
        self.num = num
        #initialize day_diagnosed
        self.day_diagnosed = day_diagnosed
        #initialize age
        self.age = age
        #initialize sex_gender
        #make all the gender to be uppercased
        sex_gender = sex_gender.upper()
        #change all the gender to M, F, or X
        if (sex_gender == "M" or sex_gender == "H" or sex_gender == "MALE" or \
           sex_gender == "BOY" or sex_gender == "HOMME" or sex_gender == "MAN"):
            self.sex_gender = "M"
        elif(sex_gender == "F" or sex_gender == "FEMME" or sex_gender == "GIRL"\
             or sex_gender == "FEMALE" or sex_gender == "WOMAN"):
            self.sex_gender = "F"
        else:
            self.sex_gender = "X"
        #initialize postal code
        first_letter = postal[0:1]
        second_letter = postal[1:2]
        third_letter = postal[2:3]
        #check whether the postal code is valid
        if(first_letter == "H" and second_letter in NUM and third_letter in LET):
            #if yes, get the first three letter of the postal code
            self.postal = postal[0:3]
        else:
            #if no, set it to be 000
            self.postal = "000"
        #initialize state
        self.state = state
        #initialize temp
        #check whether the temp is valid
        if(temps[0:1]in LET):
            temps = 0
        #change all the french , to .
        else:
            if("," in temps):
                temps = temps.replace(",", ".")
            #cut all characters that are not numbers
            for char in temps:
                if (char not in NUM and char != "."):
                    temps = temps.replace(char, "")
        i_temps = float(temps)
        #convert temps over 45 to be celcius
        if(i_temps > 45):
            i_temps = round((i_temps-32)/1.8, 2)
        self.temps = [str(i_temps)]
        #initialize days_symptomatic
        self.days_symptomatic = days_symptomatic
        
    def __str__(self):
        '''
        >>> p = Patient('0', '0', '42', 'Woman', 'H3Z2B5', 'I', '102.2', '12')
        >>> str(p)
        '0\\t42\\tF\\tH3Z\\t0\\tI\\t12\\t39.0'
        '''
        num_temp = []
        s_temps = ""
        #use ; to connect different temps
        if(len(self.temps)> 1):
            for element in self.temps:
                num_temp.append(str(element))
            s_temps = ";".join(num_temp)
        else:
            for element in self.temps:
                s_temps = s_temps + str(element)
        #use \t to connect all the elements
        info = [str(self.num), str(self.age), str(self.sex_gender), \
                str(self.postal), str(self.day_diagnosed), str(self.state), \
                str(self.days_symptomatic), str(s_temps)]
        return("\t".join(info))

    def update(self, o_patient):
        '''
        >>> p = Patient('0', '0', '42', 'Woman', 'H3Z2B5', 'I', '102.2', '12')
        >>> p1 = Patient('0', '1', '42', 'F', 'H3Z', 'I', '40,0 C', '13')
        >>> p.update(p1)
        >>> str(p)
        '0\\t42\\tF\\tH3Z\\t0\\tI\\t13\\t39.0;40.0'
        '''
        #if the input is valid
        if(self.num == o_patient.num and self.sex_gender == o_patient.sex_gender\
           and self.postal == o_patient.postal):
            #if yes, update the days_symptomatic, state, and temps
            self.days_symptomatic = o_patient.days_symptomatic
            self.state = o_patient.state
            self.temps = self.temps + o_patient.temps
        else:
            #if no, raise the error
            raise AssertionError("Wrong num or sex_gender or postal")
            
      
def stage_four(input_filename, output_filename):
    '''
    >>> p = stage_four('stage3.txt', 'stage4.txt')
    >>> str(p["0"])
    '0\\t18\\tM\\tH4A\\t0\\tR\\t5\\t38.0;38.0;37.67;37.67;38.0'
    '''
    input_file = open(input_filename, 'r')
    output_file = open(output_filename, 'w+', encoding = 'utf-8')
    new_dict = {}
    list_object = []
    list_file = input_file.readlines()
    list_key = []
    #loop through every element to get the patient object
    for i in range(len(list_file)):
        row = list_file[i].split('\t')
        if(row[1] not in new_dict):
            num = row[1]
            day_diagnosed = row[2]
            age = row[3]
            sex_gender = row[4]
            postal = row[5]
            state = row[6]
            temps = row[7]
            days_symptomatic = row[8].strip("\n")
            p = Patient(num, day_diagnosed, age, \
                        sex_gender, postal, state, temps, days_symptomatic)
        else:
            continue
        #then compare with every new entry after it to update
        for j in range(i+1, len(list_file)):
            row2 = list_file[j].split('\t')
            num2 = row2[1]
            day_diagnosed2 = row2[2]
            age2 = row2[3]
            sex_gender2 = row[4]
            postal2 = row2[5]
            state2 = row2[6]
            temps2 = row2[7]
            days_symptomatic2 = row2[8].strip("\n")
            p1 = Patient(num2, day_diagnosed2, age2,\
                         sex_gender2, postal2, state2, temps2, days_symptomatic2)
            if(row[1] == row2[1]):
                p.update(p1)
        #set the dictionary as [num:patient]
        new_dict[row[1]] = p
    #put all the key in a list
    for key in new_dict:
        list_key = list_key + [int(key)]
    #sort the key in order
    s_list_key = sorted(list_key)
    #write values of dict according to the sorted key
    for element in s_list_key:
        output_file.write(str(new_dict[str(element)]) + "\n")
    return new_dict



def fatality_by_age(d):
    '''
    >>> p = stage_four('stage3.txt', 'stage4.txt')
    >>> fatality_by_age(p)
    [1.0, 0.7857142857142857, 0.9, 0.8461538461538461, 0.8333333333333334, 0.75, 1.0, 0.9523809523809523, 0.9230769230769231, 0.8888888888888888, 0.85, 0.9333333333333333, 0.9333333333333333, 0.9090909090909091, 0.75, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    '''
    
    age_list = []
    n_age_list = []
    double_dict = {}
    prob_list = []
    #round all the ages to their nearest 5 and append all the ages to a list
    for key in d:
        d[key].age = str(5*round(int(d[key].age)/5))
        age_list.append(int(d[key].age))
    #eliminate the repeated age groups
    for i in age_list:
        if i not in n_age_list:
            n_age_list.append(i)
    #sort the age groups accordings to its order
    s_age_list = sorted(n_age_list)    
    np_x = np.array(s_age_list)
    #set all all age group to be key to calculate how many recovered and died patients are in
    #that specific age group
    for element in s_age_list:
        double_dict[str(element)] = {"R":0, "M":0}
    for key in d:
        if(d[key].state == "R" or d[key].state == "M"):
            double_dict[d[key].age][d[key].state] = double_dict[d[key].age]\
                                                    [d[key].state] + 1
    #calculate all the probability and add them to a list
    for keyD in double_dict:
        keyM = double_dict[keyD]["M"]
        keyR = double_dict[keyD]["R"]
        if(keyM + keyR != 0):
            prob_list.append(float(double_dict[keyD]["M"]/\
                                 (double_dict[keyD]["M"] \
                                  + double_dict[keyD]["R"])))
        else:
            prob_list.append(float(1))
    #draw the graph
    np_y = np.array(prob_list)
    plt.plot(np_x, np_y, "b")
    plt.title("Probability of death vs age, by Yimei Yang")
    plt.xlabel('Age')
    plt.ylabel("Deaths/(Deaths+Recoveries)")
    plt.ylim((0, 1.2))
    plt.savefig("fatality_by_age.png")
    #return the probability list
    return prob_list
        
        
        



        
    
        
        

    
        
        
        
        
       
    
    

if __name__ == '__main__':
    doctest.testmod()

        
