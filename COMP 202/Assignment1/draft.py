import doctest
from unit_conversion import *

def fp_from_vegan():
    annual_CO2E_kg = 2.89*365.2425;
    annual_CO2E_ton = kg_to_tonnes(annual_CO2E_kg);
    print(annual_CO2E_ton);

def fp_from_meat(daily_g_meat):
    daily_CO2E_g = daily_g_meat*26.8;
    annual_CO2E_g = daily_to_annual(daily_CO2E_g);
    annual_CO2E_ton = kg_to_tonnes(annual_CO2E_g/1000);
    print(annual_CO2E_ton);

def fp_from_cheese(daily_g_cheese):
    daily_CO2E_g = daily_g_cheese*12;
    annual_CO2E_g = daily_to_annual(daily_CO2E_g);
    annual_CO2E_ton = kg_to_tonnes(annual_CO2E_g/1000);
    print(annual_CO2E_ton);

def fp_from_milk(daily_L_milk):
    daily_CO2E_g = daily_L_milk*267.777;
    annual_CO2E_g = daily_to_annual(daily_CO2E_g);
    annual_CO2E_ton = kg_to_tonnes(annual_CO2E_g/1000);
    print(annual_CO2E_ton);

def fp_from_egg(daily_num_eggs):
    daily_CO2E_g = daily_num_eggs*300;
    annual_CO2E_g = daily_to_annual(daily_CO2E_g);
    annual_CO2E_ton = kg_to_tonnes(annual_CO2E_g/1000);
    print(annual_CO2E_ton);

fp_from_vegan()
fp_from_meat(10)
fp_from_meat(20)
fp_from_cheese(10)
fp_from_cheese(20)
fp_from_milk(10)
fp_from_milk(20)
fp_from_egg(10)
fp_from_egg(20)
