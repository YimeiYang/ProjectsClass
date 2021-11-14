# COMP 202 A3 Part 1
# Name:Yimei Yang
# Student ID: 260898303

import doctest
import random

def flatten_lists(nested):
    '''
    (list)-->list
    Combine all the elements in the nested list into a list
    >>> flatten_lists([[0], [1, 2], [3]])
    [0, 1, 2, 3]
    >>> flatten_lists([1, [3, 4]])
    [1, [3, 4]]
    >>> flatten_lists([["a", -4, -5], ["4",3, "H"]])
    ['a', -4, -5, '4', 3, 'H']
    >>> flatten_lists(["a", 12, 2])
    ['a', 12, 2]
    '''
    #create a new list
    New_list = [ ]
    #loop through all the elements in the nested list
    for lists in nested:
        if (type(lists) == list):
            for element in lists:
                #append all the element into the new list
                New_list.append(element)
        else:
            return nested
    return New_list

def flatten_dict(d):
    '''
    (dict)-->list
    return a list of the keys of the dictionary, repeated v many times,
    where v is the value associated with the key in the dictionary.
    >>> flatten_dict({'LIBERAL': 5, 'NDP': 2})
    ['LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'NDP', 'NDP']
    >>> flatten_dict({'GREEN': 3, 'CPC': 1})
    ['GREEN', 'GREEN', 'GREEN', 'CPC']
    >>> flatten_dict({'BLOC': 2, 'NDP':1})
    ['BLOC', 'BLOC', 'NDP']
    '''
    #create a new list
    New_list_key = [ ]
    #loop through all the keys in the dictionary
    for key in d:
        count = 0
        while(d[key]!= count):
            #append the keys n times until n=v
            New_list_key.append(key)
            count = count + 1
    return New_list_key
            

def add_dicts(d1, d2):
    '''
    Add two dictionaries together
    (dict, dict)-->dict
    >>> add_dicts({'a': 5, 'b': 2, 'd': -1}, {'a': 7, 'b': 1, 'c': 5})
    {'a': 12, 'b': 3, 'd': -1, 'c': 5}
    >>> add_dicts({'a':5, 'b':2, 'c':-1}, {'e': 7, 'f': 1, 'g': 5})
    {'a': 5, 'b': 2, 'c': -1, 'e': 7, 'f': 1, 'g': 5}
    >>> add_dicts({'e':5, 'b':2, 'd':-1}, {'a':7, 'b':1, 'c':5})
    {'e': 5, 'b': 3, 'd': -1, 'a': 7, 'c': 5}
    '''
    #create a new dictionary
    New_dict = { }
    #loop through the first dictionary and add the value of the same key in d2
    for key in d1:
        if key in d2:
            New_dict[key] = d1[key] + d2[key]
        else:
            New_dict[key] = d1[key]
    #loop through the second dictionary and add the key-value pairs that
    #does not exist in the new dictionary
    for key in d2:
        if key in New_dict:
            continue
        else:
            New_dict[key] = d2[key]
    return New_dict

def get_all_candidates(ballots):
    '''
    (dict/str/list)-->list
    Combine all the keys in the input into a list
    >>> get_all_candidates([{'GREEN': 3, 'NDP': 5}, \
                        {'NDP': 2, 'LIBERAL': 4}, ['CPC', 'NDP'], 'BLOC'])
    ['GREEN', 'NDP', 'LIBERAL', 'CPC', 'BLOC']
    >>> get_all_candidates([{'LIBERAL': 3, 'NDP': 5}, \
                        {'GREEN': 2}, ['NDP']])
    ['LIBERAL', 'NDP', 'GREEN']
    >>> get_all_candidates([['LIBERAL'], ['GREEN', 'NDP'], ['LIBERAL']])
    ['LIBERAL', 'GREEN', 'NDP']
    '''
    #create new lists
    New_element_list = [ ]
    New_unique_list = [ ]
    #loop through all the elements in the input and append the element into the
    #new list according to their different attribution 
    for element in ballots:
        if (type(element) == str):
            New_element_list.append(element)
        elif(type(element) == list):
            for char in element:
                New_element_list.append(char)
        else:
            for key in element:
                New_element_list.append(key)
    #loop through the new list and get rid of the repeated elements
    for element in New_element_list:
        if element in New_unique_list:
            continue
        else:
            New_unique_list.append(element)
            
    return New_unique_list
        
            


###################################################### winner/loser

def get_candidate_by_place(result, func):
    '''
    Evaluate the function on the dictionary’s values. Return the
    key of the dictionary corresponding to that value.
    (dict, func) --> str
    >>> result = {'LIBERAL': 10, 'NDP': 6, 'CPC': 4, 'GREEN': 4}
    >>> random.seed(0)
    >>> get_candidate_by_place(result, min)
    'GREEN'
    >>> random.seed(1)
    >>> get_candidate_by_place(result, min)
    'CPC'
    >>> get_candidate_by_place({}, min)
    False
    >>> get_candidate_by_place({'LIBERAL': 1}, max)
    'LIBERAL'
    '''
    #create a new list
    New_random_list = [ ]
    New_value_list = [ ]
    empty_dict = {}
    if len(result)!=0:
    #put all the values into a list
        New_value_list = result.values()
    #find the max/min value in the list
        M = func(New_value_list)
    #find the keys corresponding to the value
        for key in result:
        #break the ties randomly
            if (result[key] == M):
                New_random_list.append(key)
        rN = random.randint(0, len(New_random_list)-1)
        return New_random_list[rN]
    else:
        return False
    


def get_winner(result):
    '''
    Return the key with the greatest value.
    If there are ties, break them randomly.
    (dict) --> str
    >>> result = {'LIBERAL': 10, 'NDP': 10, 'CPC': 4, 'GREEN': 4}
    >>> random.seed(0)
    >>> get_winner(result)
    'NDP'
    >>> random.seed(1)
    >>> get_winner(result)
    'LIBERAL'
    >>> get_winner({})
    False
    >>> get_winner({'LIBERAL': 1})
    'LIBERAL'
    '''
    #implement the max function
    empty_dict = {}
    if(len(result)!=0):
        return get_candidate_by_place(result, max)
    #if the input is an empty dict, return false
    else:
        return False

def last_place(result, seed = None):
    '''
    Return the key with the lowest value.
    If there are ties, break them randomly.
    (dict) --> str
    >>> result = {'LIBERAL': 10, 'NDP': 6, 'CPC': 4, 'GREEN': 4}
    >>> random.seed(0)
    >>> last_place(result)
    'GREEN'
    >>> random.seed(1)
    >>> last_place(result)
    'CPC'
    >>> last_place({})
    False
    >>> last_place({'LIBERAL': 1})
    'LIBERAL'
    '''
    #implement the max function
    empty_dict = {}
    if(len(result)!=0):
        return get_candidate_by_place(result, min)
    #if the input is an empty dict, return false
    else:
        return False


###################################################### testing help

def pr_dict(d):
    '''(dict) -> None
    Print d in a consistent fashion (sorted by key).
    Provided to students. Do not edit.
    >>> pr_dict({'a':1, 'b':2, 'c':3})
    {'a': 1, 'b': 2, 'c': 3}
    '''
    l = []
    for k in sorted(d):
        l.append( "'" + k + "'" + ": " + str(d[k]) )
    print('{' + ", ".join(l) + '}')


if __name__ == '__main__':
    doctest.testmod()
