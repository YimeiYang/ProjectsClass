# COMP 202 A3
# Name: Yimei Yang
# ID: 260898303
import math
from single_winner import *

################################################################################

def votes_needed_to_win(ballots, num_winners):
    '''
    >>> votes_needed_to_win([{'CPC':3, 'NDP':5}, {'NDP':2, 'CPC':4}, \
    {'CPC':3, 'NDP':5}], 1)
    2
    >>> votes_needed_to_win(['g']*20, 2)
    7
    '''
    #get the total number of votes as the length of input
    total_num = len(ballots)
    #round down
    round_down = math.floor(total_num/(num_winners+1)+1)
    return round_down
    


def has_votes_needed(result, votes_needed):
    '''
    >>> has_votes_needed({'NDP': 4, 'LIBERAL': 3}, 4)
    True
    >>> has_votes_needed({}, 2)
    False
    >>> has_votes_needed({'LIBERAL': 2}, 3)
    True
    '''
    #if there are more than one candidates, compare their votes with votes_needed
    if(len(result) >1):
        Max = get_winner(result)
        return (result[Max] >= votes_needed)
    #if there is only one candidate, the candidate is the winner
    elif (len(result)==1):
        return True
    #if the input is empty, return false
    else:
        return False
    


################################################################################


def eliminate_candidate(ballots, to_eliminate):
    '''
    >>> eliminate_candidate([['NDP', 'LIBERAL'], ['GREEN', 'NDP'], \
    ['NDP', 'BLOC']], ['NDP', 'LIBERAL'])
    [[], ['GREEN'], ['BLOC']]
    >>> eliminate_candidate([['NDP', 'LIBERAL'], ['GREEN', 'NDP'], \
    ['NDP', 'BLOC']], ['NDP', 'LIBERAL'])
    [[], ['GREEN'], ['BLOC']]
    '''
    element_need = []
    #loop through all elements in the input
    for index, element in enumerate(ballots):
        value_need = []
        #add elements that are not in the to_eliminate list
        for value in element:
            if value not in to_eliminate:
                value_need.append(value)
        element_need.append(value_need)
    return element_need

################################################################################


def count_irv(ballots):
    '''
    >>> pr_dict(count_irv([['NDP'], ['GREEN', 'NDP', 'BLOC'], ['LIBERAL','NDP'],\
    ['LIBERAL'], ['NDP', 'GREEN'], ['BLOC', 'GREEN', 'NDP'],\
    ['BLOC', 'CPC'], ['LIBERAL', 'GREEN'], ['NDP']]))
    {'BLOC': 0, 'CPC': 0, 'GREEN': 0, 'LIBERAL': 3, 'NDP': 5}
    >>> pr_dict(count_irv([['GREEN'], ['LIBERAL', 'CPC'], \
    ['BLOC', 'LIBERAL'],['GREEN'], ['CPC', 'LIBERAL']]))
    {'BLOC': 0, 'CPC': 0, 'GREEN': 2, 'LIBERAL': 3}
    >>> pr_dict(count_irv([['GREEN'], ['LIBERAL', 'GREEN'], \
    ['GREEN', 'LIBERAL'], ['GREEN'], ['GREEN', 'LIBERAL']]))
    {'GREEN': 4, 'LIBERAL': 1}
    >>> pr_dict(count_irv([['NDP'], ['NDP'],\
    ['LIBERAL', 'NDP'], ['LIBERAL'], ['NDP'],\
    ['NDP'], ['LIBERAL'], ['NDP']]))
    {'LIBERAL': 3, 'NDP': 5}
    '''
    
    eliminate_list = []
    #loop until one candidate is the majority
    while (not has_votes_needed(count_first_choices(ballots),\
                               votes_needed_to_win\
                               (ballots, 1))):
        first_element_dict = count_first_choices(ballots)
        #get the last place candidate
        last_place_variable = [last_place(first_element_dict, seed=None)]
        #eliminate the last place candidate
        ballots = eliminate_candidate(ballots, last_place_variable)
        eliminate_list = eliminate_list + last_place_variable
    #get the updated first choice dictionary
    first_element_new = count_first_choices(ballots)
    
    be_eliminated = count_approval(eliminate_list)
    #add candidates that are eliminated to the dictionary
    for element in be_eliminated:
        be_eliminated[element] = 0

    result = add_dicts(be_eliminated, first_element_new)
    return result
                                                 
        


################################################################################

if __name__ == '__main__':
    doctest.testmod()
