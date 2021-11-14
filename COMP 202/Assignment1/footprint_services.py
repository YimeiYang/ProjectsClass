# COMP 202 A1: Part 2
# Footprint of utilities & university
# Author: Yimei Yang 260898303

import doctest
from unit_conversion import *

INCOMPLETE = -1

######################################### Utilities

def fp_from_gas(monthly_gas):
    '''(num) -> float
    Calculate metric tonnes of CO2E produced annually
    based on monthly natural gas bill in $.

    Source: https://www.forbes.com/2008/04/15/green-carbon-living-forbeslife-cx_ls_0415carbon.html#1f3715d01852
        B.) Multiply your monthly gas bill by 105 [lbs, to get annual amount] 

    >>> fp_from_gas(0)
    0.0
    >>> round(fp_from_gas(100), 4)
    4.7627
    >>> round(fp_from_gas(25), 4)
    1.1907
    '''
    #Multiply to get annual amount in lbs
    Annual_lbs = monthly_gas*105;
    #Convert lbs to tonnes
    Annual_tonnes = kg_to_tonnes(pound_to_kg(Annual_lbs));
    return Annual_tonnes;



def fp_from_hydro(daily_hydro):
    '''(num) -> float
    Calculate metric tonnes of CO2E produced annually
    based on average daily hydro usage.

    To find out your average daily hydro usage in kWh:
        Go to https://www.hydroquebec.com/portail/en/group/clientele/portrait-de-consommation
        Scroll down to "Annual total" and press "kWh"

    Source: https://www.hydroquebec.com/data/developpement-durable/pdf/co2-emissions-electricity-2017.pdf
        0.6 kg CO2E / MWh

    >>> fp_from_hydro(0)
    0.0
    >>> round(fp_from_hydro(10), 4)
    0.0022
    >>> round(fp_from_hydro(48.8), 4)
    0.0107
    '''
    #Calculate annual CO2E emission
    annual_hydro = daily_to_annual(daily_hydro);
    annual_CO2E_kg = (annual_hydro/1000)*0.6;
    #Convert kg to ton
    annual_CO2E_tonnes = kg_to_tonnes(annual_CO2E_kg);
    return annual_CO2E_tonnes;



def fp_of_utilities(daily_hydro, monthly_gas):
    '''(num, num, num) -> float
    Calculate metric tonnes of CO2E produced annually from
    daily hydro (in kWh) and gas bills (in $) and monthly phone data (in GB).

    >>> fp_of_utilities(0, 0)
    0.0
    >>> round(fp_of_utilities(100, 0), 4)
    0.0219
    >>> round(fp_of_utilities(0, 100), 4)
    4.7627
    >>> round(fp_of_utilities(50, 20), 4)
    0.9635
    '''
    #Calculate the sum of annual CO2E emission of hydro and gas
    annual_GasAndHydro_tonnes = fp_from_hydro(daily_hydro)+fp_from_gas(monthly_gas);
    return annual_GasAndHydro_tonnes;


#################################################


def fp_of_studies(annual_uni_credits):
    '''(num, num, num) -> flt
    Return metric tonnes of CO2E from being a student, based on
    annual university credits.

    Source: https://www.mcgill.ca/facilities/files/facilities/ghg_inventory_report_2017.pdf
        1.12 tonnes per FTE (30 credit) student

    >>> round(fp_of_studies(0), 4)
    0.0
    >>> round(fp_of_studies(30), 4)
    1.12
    >>> round(fp_of_studies(18), 4)
    0.672
    '''
    #Calculate FTE for each students
    per_FTE = annual_uni_credits/30;
    #Calculate their annual CO2E emission 
    tonnes_per_student = per_FTE*1.12;
    return tonnes_per_student;


#################################################

if __name__ == '__main__':
    doctest.testmod()
