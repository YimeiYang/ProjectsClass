# COMP 202 A1: Part 4
# Footprint of computing and diet
# Author: Yimei Yang 260898303

import doctest
from unit_conversion import *

INCOMPLETE = -1

######################################
#helper functions

#calculate the CO2E from online 
def fp_from_online(daily_online_use):
    '''(num) ->flt
Estimate in annual CO2E tonnes from being online.
>>> fp_from_online(0)
0.0
>>> round(fp_from_online(10),4)
0.2009
>>> round(fp_from_online(20),4)
0.4018
'''
    daily_CO2E_g = daily_online_use*55;
    annual_CO2E_g = daily_to_annual(daily_CO2E_g);
    annual_CO2E_ton = kg_to_tonnes(annual_CO2E_g/1000);
    return annual_CO2E_ton;
#calculate the CO2E from phone using
def fp_from_phone(daily_phone_use):
    '''(num) ->flt
Estimate in annual CO2E tonnes from phones.
>>> fp_from_online(0)
0.0
>>> round(fp_from_phone(10),4)
12.5
>>> round(fp_from_phone(20),4)
25.0
'''
    annual_CO2E_kg = daily_phone_use*1250;
    annual_CO2E_ton = kg_to_tonnes(annual_CO2E_kg);
    return annual_CO2E_ton;
#calculate the CO2E from light Devices 
def fp_from_lightDevices(new_light_devices):
    '''(num) ->flt
Estimate in annual CO2E tonnes from light devices.
>>> fp_from_lightDevices(0)
0.0
>>> round(fp_from_lightDevices(10),4)
0.75
>>> round(fp_from_lightDevices(20),4)
1.5
'''
    annual_CO2E_kg = new_light_devices*75;
    annual_CO2E_ton = kg_to_tonnes(annual_CO2E_kg);
    return annual_CO2E_ton;
#calculate the CO2E from medium devices
def fp_from_mediumDevices(new_medium_devices):
    '''(num) ->flt
Estimate in annual CO2E tonnes from medium devices.
>>> fp_from_mediumDevices(0)
0.0
>>> round(fp_from_mediumDevices(10),4)
2.0
>>> round(fp_from_mediumDevices(20),4)
4.0
'''
    annual_CO2E_kg = new_medium_devices*200;
    annual_CO2E_ton = kg_to_tonnes(annual_CO2E_kg);
    return annual_CO2E_ton;
#calculate the CO2E from heavy devices
def fp_from_heavyDevices(new_heavy_devices):
    '''(num) ->flt
Estimate in annual CO2E tonnes from heavy devices.
>>> fp_from_heavyDevices(0)
0.0
>>> round(fp_from_heavyDevices(10),4)
8.0
>>> round(fp_from_heavyDevices(20),4)
16.0
'''
    annual_CO2E_kg = new_heavy_devices*800;
    annual_CO2E_ton = kg_to_tonnes(annual_CO2E_kg);
    return annual_CO2E_ton;
######################################

def fp_of_computing(daily_online_use, daily_phone_use,
                    new_light_devices, new_medium_devices, new_heavy_devices):
    '''(num, num) -> float

    Metric tonnes of CO2E from computing, based on daily hours of online & phone use, and how many small (phone/tablet/etc) & large (laptop) & workstation devices you bought.

    Source for online use: How Bad Are Bananas
        55 g CO2E / hour

    Source for phone use: How Bad Are Bananas
        1250 kg CO2E for a year of 1 hour a day

    Source for new devices: How Bad Are Bananas
        200kg: new laptop
        800kg: new workstation
        And from: https://www.cnet.com/news/apple-iphone-x-environmental-report/
        I'm estimating 75kg: new small device

    >>> fp_of_computing(0, 0, 0, 0, 0)
    0.0
    >>> round(fp_of_computing(6, 0, 0, 0, 0), 4)
    0.1205
    >>> round(fp_of_computing(0, 1, 0, 0, 0), 4)
    1.25
    >>> fp_of_computing(0, 0, 1, 0, 0)
    0.075
    >>> fp_of_computing(0, 0, 0, 1, 0)
    0.2
    >>> fp_of_computing(0, 0, 0, 0, 1)
    0.8
    >>> round(fp_of_computing(4, 2, 2, 1, 1), 4)
    3.7304
    '''
    #Sum up the annual CO2E of online using, phone using, and
    #buying light, medium, and heavy devices.
    annual_CO2E_ton_computing = fp_from_online(daily_online_use)+\
                                fp_from_phone(daily_phone_use)+\
                                fp_from_lightDevices(new_light_devices)+\
                                fp_from_mediumDevices(new_medium_devices)+\
                                fp_from_heavyDevices(new_heavy_devices);
    return annual_CO2E_ton_computing;


######################################
#helper functions

#calculate the CO2E from vegan 
def fp_from_vegan():
    '''()
Estimate in annual CO2E tonnes from vegan.
>>> round(fp_from_vegan(),4)
1.0556
'''
    annual_CO2E_kg = 2.89*365.2425;
    annual_CO2E_ton = kg_to_tonnes(annual_CO2E_kg);
    return annual_CO2E_ton;
#calculate the CO2E from meat
def fp_from_meat(daily_g_meat):
    '''(num) ->flt
Estimate in annual CO2E tonnes from meat.
>>> fp_from_meat(0)
0.0
>>> round(fp_from_meat(10),4)
0.0979
>>> round(fp_from_meat(20),4)
0.1958
'''
    daily_CO2E_g = daily_g_meat*26.8;
    annual_CO2E_g = daily_to_annual(daily_CO2E_g);
    annual_CO2E_ton = kg_to_tonnes(annual_CO2E_g/1000);
    return annual_CO2E_ton;
#calculate the CO2E from cheese
def fp_from_cheese(daily_g_cheese):
    '''(num) ->flt
Estimate in annual CO2E tonnes from cheese.
>>> fp_from_meat(0)
0.0
>>> round(fp_from_cheese(10),4)
0.0438
>>> round(fp_from_cheese(20),4)
0.0877
'''
    daily_CO2E_g = daily_g_cheese*12;
    annual_CO2E_g = daily_to_annual(daily_CO2E_g);
    annual_CO2E_ton = kg_to_tonnes(annual_CO2E_g/1000);
    return annual_CO2E_ton;
#calculate the CO2E from milk
def fp_from_milk(daily_L_milk):
    '''(num) ->flt
Estimate in annual CO2E tonnes from milk.
>>> fp_from_meat(0)
0.0
>>> round(fp_from_milk(10),4)
0.978
>>> round(fp_from_milk(20),4)
1.9561
'''
    daily_CO2E_g = daily_L_milk*267.777;
    annual_CO2E_g = daily_to_annual(daily_CO2E_g);
    annual_CO2E_ton = kg_to_tonnes(annual_CO2E_g/1000);
    return annual_CO2E_ton;
#calculate the CO2E from eggs
def fp_from_egg(daily_num_eggs):
    '''(num) ->flt
Estimate in annual CO2E tonnes from eggs.
>>> fp_from_egg(0)
0.0
>>> round(fp_from_egg(10),4)
1.0957
>>> round(fp_from_egg(20),4)
2.1915
'''
    daily_CO2E_g = daily_num_eggs*300;
    annual_CO2E_g = daily_to_annual(daily_CO2E_g);
    annual_CO2E_ton = kg_to_tonnes(annual_CO2E_g/1000);
    return annual_CO2E_ton;
    
    
######################################

def fp_of_diet(daily_g_meat, daily_g_cheese, daily_L_milk, daily_num_eggs):
    '''
    (num, num, num, num) -> flt
    Approximate annual CO2E footprint in metric tonnes, from diet, based on daily consumption of meat in grams, cheese in grams, milk in litres, and eggs.

    Based on https://link.springer.com/article/10.1007%2Fs10584-014-1169-1
    A vegan diet is 2.89 kg CO2E / day in the UK.
    I infer approximately 0.0268 kgCO2E/day per gram of meat eaten.

    This calculation misses forms of dairy that are not milk or cheese, such as ice cream, yogourt, etc.

    From How Bad Are Bananas:
        1 pint of milk (2.7 litres) -> 723 g CO2E 
                ---> 1 litre of milk: 0.2677777 kg of CO2E
        1 kg of hard cheese -> 12 kg CO2E 
                ---> 1 g cheese is 12 g CO2E -> 0.012 kg CO2E
        12 eggs -> 3.6 kg CO2E 
                ---> 0.3 kg CO2E per egg

    >>> round(fp_of_diet(0, 0, 0, 0), 4) # vegan
    1.0556
    >>> round(fp_of_diet(0, 0, 0, 1), 4) # 1 egg
    1.1651
    >>> round(fp_of_diet(0, 0, 1, 0), 4) # 1 L milk
    1.1534
    >>> round(fp_of_diet(0, 0, 1, 1), 4) # egg and milk
    1.2629
    >>> round(fp_of_diet(0, 10, 0, 0), 4) # cheeese
    1.0994
    >>> round(fp_of_diet(0, 293.52, 1, 1), 4) # egg and milk and cheese
    2.5494
    >>> round(fp_of_diet(25, 0, 0, 0), 4) # meat
    1.3003
    >>> round(fp_of_diet(25, 293.52, 1, 1), 4) 
    2.7941
    >>> round(fp_of_diet(126, 293.52, 1, 1), 4)
    3.7827
    '''
    #Sum up the annual CO2E of daily consumption
    annual_CO2E_ton_consumption = fp_from_vegan()+\
                                  fp_from_meat(daily_g_meat)+\
                                  fp_from_cheese(daily_g_cheese)+\
                                  fp_from_milk(daily_L_milk)+\
                                  fp_from_egg(daily_num_eggs);
                                               
    return annual_CO2E_ton_consumption;


#################################################

if __name__ == '__main__':
    doctest.testmod()

