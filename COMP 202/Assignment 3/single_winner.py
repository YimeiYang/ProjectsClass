# COMP 202 A3
# Name: Yimei Yang
# Student ID: 260898303

from a3_helpers import *


def count_plurality(ballots):
    '''
    (list)-->dict
    Return a dictionary of how many votes each candidate got
    >>> count_plurality(['LIBERAL', 'LIBERAL', 'NDP', 'LIBERAL'])
    {'LIBERAL': 3, 'NDP': 1}
    >>> count_plurality(['LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL'])
    {'LIBERAL': 4}
    '''
    #create a new dictionary
    New_value_list = [ ] 
    New_dict = { }
    Unique_element = [ ]
    #loop through all the element in the input and put the unqiue
    #elements into a string
    all_candidates = get_all_candidates(ballots)
    for element in all_candidates:
        if element in Unique_element:
            continue
        else:
            Unique_element.append(element)
    #put unique elements in to the dictionary as keys, and times they
    #appear in the input lists as values.
    expand_list = flatten_lists(ballots)
    for element in Unique_element:
        New_value_list.append(expand_list.count(element))                
    New_dict = dict(zip(Unique_element, New_value_list))
    return New_dict
        
    

def count_approval(ballots):
    '''
    (list)-->dict
    return a dictionary of how many votes each candidate got
    >>> count_approval([['LIBERAL', 'NDP'], ['NDP'], \
                        ['NDP', 'GREEN', 'BLOC']])
    {'LIBERAL': 1, 'NDP': 3, 'GREEN': 1, 'BLOC': 1}
    >>> count_approval([['GREEN', 'NDP'], ['BLOC'], \
                        ['LIBERAL', 'GREEN', 'BLOC']])
    {'GREEN': 2, 'NDP': 1, 'BLOC': 2, 'LIBERAL': 1}
    >>> count_approval([['LIBERAL', 'BLOC'], ['NDP'], \
                        ['GREEN']])
    {'LIBERAL': 1, 'BLOC': 1, 'NDP': 1, 'GREEN': 1}
    '''
    #combine all the elements in the input into one list
    All_elements = flatten_lists(ballots)
    #return a dictionary of how many votes each candidate got
    return count_plurality(All_elements)


def count_rated(ballots):
    '''
    (list)-->dict
    return a dictionary of how many votes each candidate got
    >>> count_rated([{'LIBERAL': 5, 'NDP': 2}, {'NDP': 4, 'GREEN': 5}])
    {'LIBERAL': 5, 'NDP': 6, 'GREEN': 5}
    >>> count_rated([{'LIBERAL': 5, 'GREEN': 2}, {'NDP': 4, 'GREEN': 5}])
    {'LIBERAL': 5, 'GREEN': 7, 'NDP': 4}
    >>> count_rated([{'NDP': 2}, {'BLOC': 4, 'GREEN': 5}])
    {'NDP': 2, 'BLOC': 4, 'GREEN': 5}
    '''
    #create a new dictionary
    New_dict = { }
    #loop through all the element in the input and add each element
    #with each other
    for i in range(len(ballots)):
        New_dict = add_dicts(New_dict, ballots[i])
    return New_dict

def count_first_choices(ballots):
    '''
    (list)-->dict
    return a dictionary storing, for every party represented in \
    all the ballots, how many ballots for which that party \
    was the first choice.
    >>> count_first_choices([['NDP', 'LIBERAL'], ['GREEN', 'NDP'],\
    ['NDP', 'BLOC']])
    {'NDP': 2, 'GREEN': 1, 'LIBERAL': 0, 'BLOC': 0}
    >>> count_first_choices([['BLOC', 'LIBERAL'], ['LIBERAL', 'NDP']])
    {'BLOC': 1, 'LIBERAL': 1, 'NDP': 0}
    >>> count_first_choices([['GREEN', 'NDP'],\
    ['NDP', 'LIBERAL']])
    {'GREEN': 1, 'NDP': 1, 'LIBERAL': 0}
    >>> count_first_choices([[], ['GREEN', 'NDP'], ['LIBERAL', 'GREEN']])
    {'GREEN': 1, 'LIBERAL': 1, 'NDP': 0}
    '''
    New_lists = [ ]
    New_dict = { }
    left_dict = { }
    all_candidates = [ ]
    left_candidates = [ ]
    #loop through the input and put all the first element in each list
    #into a new list
    for lists in ballots:
        if (len(lists) == 0):
            continue
        else:
            New_lists.append(lists[0])
    #put the first place candidates into dictionary
    New_dict = count_plurality(New_lists)
    all_candidates = flatten_lists(ballots)
    #substract all the firt place candidates in the input list to get
    #all the other candidates
    for element in all_candidates:
        if element in New_lists:
            continue
        else:
            left_candidates.append(element)
    #put other candidates into a dictionary
    for element in left_candidates:
        left_dict[element] = 0
    #add the first place dictionary and the other candidates dictionary
        #together
    return add_dicts(New_dict, left_dict)
    
    
    

if __name__ == '__main__':
    doctest.testmod()
