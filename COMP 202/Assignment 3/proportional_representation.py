# COMP 202 A3
# Name: Yimei Yang
# Student ID: 260898303

from instant_run_off import *

################################################################################

def irv_to_stv_ballot(ballots, num_winners):
    '''
    For every ranked ballot: replace each party with \
    num winners many candidates from that party, numbering them starting from 0
    >>> irv_to_stv_ballot([['NDP', 'CPC'], ['GREEN']], 3)
    [['NDP0', 'NDP1', 'NDP2', 'CPC0', 'CPC1', 'CPC2'], ['GREEN0', 'GREEN1', 'GREEN2']]
    '''
    new_list = []
    #loop through elements in the input
    for index, element in enumerate(ballots):
        new_indi_list = []
        #number them starting from 0
        for value in element:
            for i in range(num_winners):
                new_indi_list.append(value+str(i))
        new_list.append(new_indi_list)
    return new_list
            
            
            


################################################################################


def eliminate_n_ballots_for(ballots, to_eliminate, n):
    '''(lst, str) -> lst
    Remove n of the ballots in ballots where the first choice is for the candidate to_eliminate.

    Provided to students. Do not edit.

    >>> ballots = [['GREEN1', 'GREEN2', 'GREEN3'], ['GREEN1', 'GREEN2', 'GREEN3'], ['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3']]
    >>> eliminate_n_ballots_for(ballots, ['GREEN1'], 1)
    [['GREEN1', 'GREEN2', 'GREEN3'], ['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3']]
    >>> eliminate_n_ballots_for(ballots, ['GREEN1'], 2)
    [['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3']]
    >>> eliminate_n_ballots_for(ballots, ['NDP3'], 2)
    [['GREEN1', 'GREEN2', 'GREEN3'], ['GREEN1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3']]
    >>> eliminate_n_ballots_for(ballots, ['NDP3'], 1)
    [['GREEN1', 'GREEN2', 'GREEN3'], ['GREEN1', 'GREEN2', 'GREEN3'], ['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3']]
    >>> eliminate_n_ballots_for(ballots, ['NDP3', 'GREEN1'], 5)
    [['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3']]
    >>> b = [['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3'], ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3'], ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3']]
    >>> eliminate_n_ballots_for(b, ['GREEN1'], 2)
    [['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3'], ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3'], ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3']]
    '''
    quota = n
    new_ballots = []
    elims = 0
    for i,b in enumerate(ballots):
        if (elims >= quota) or  (len(b) > 0 and b[0] not in to_eliminate):
            new_ballots.append(b)
        else:
            elims += 1
    return new_ballots



def stv_vote_results(ballots, num_winners):
    '''(lst of list, int) -> dict

    From the ballots, elect num_winners many candidates using Single-Transferable Vote
    with Droop Quota. Return how many votes each candidate has at the end of all transfers.
    
    Provided to students. Do not edit.

    >>> random.seed(3) # make the random tie-break consistent
    >>> g = ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1']
    >>> n = ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3']
    >>> pr_dict(stv_vote_results([g]*5 + [n]*3, 4))
    {'BLOC1': 0, 'GREEN1': 2, 'GREEN2': 2, 'GREEN3': 0, 'NDP1': 2, 'NDP2': 2, 'NDP3': 0}
    >>> random.seed(1)
    >>> pr_dict(stv_vote_results([g]*5 + [n]*3, 4))
    {'BLOC1': 0, 'GREEN1': 2, 'GREEN2': 2, 'GREEN3': 0, 'NDP1': 2, 'NDP2': 0, 'NDP3': 0}
    >>> green = ['GREEN', 'NDP', 'BLOC', 'LIBERAL', 'CPC']
    >>> ndp = ['NDP', 'GREEN', 'BLOC', 'LIBERAL', 'CPC']
    >>> liberal = ['LIBERAL', 'CPC', 'GREEN', 'NDP', 'BLOC']
    >>> cpc = ['CPC', 'NDP', 'LIBERAL', 'BLOC', 'GREEN']
    >>> bloc = ['BLOC', 'NDP', 'GREEN', 'CPC', 'LIBERAL']
    >>> pr_dict(stv_vote_results([green]*10 + [ndp]*20 + [liberal]*15 + [cpc]*30 + [bloc]*25, 2))
    {'BLOC': 32, 'CPC': 34, 'GREEN': 0, 'LIBERAL': 0, 'NDP': 34}
    >>> pr_dict(stv_vote_results([green]*10 + [ndp]*20 + [liberal]*15 + [cpc]*30 + [bloc]*25, 3))
    {'BLOC': 26, 'CPC': 26, 'GREEN': 0, 'LIBERAL': 22, 'NDP': 26}
    '''
    quota = votes_needed_to_win(ballots, num_winners)

    to_eliminate = []
    result = {}
    final_result = {}

    for i in range(num_winners):
        # start off with quasi-IRV

        result = count_first_choices(ballots)

        while (not has_votes_needed(result, quota)) and len(result) > 0:
            to_eliminate.append( last_place(result) ) 
            ballots = eliminate_candidate(ballots, to_eliminate)
            result = count_first_choices(ballots)

        # but now with the winner, reallocate ballots above quota and keep going
        winner = get_winner(result)
        if winner:
            final_result[winner] = quota # winner only needs quota many votes
            ballots = eliminate_n_ballots_for(ballots, final_result.keys(), \
                                              quota)
            ballots = eliminate_candidate(ballots, final_result.keys())
            result = count_first_choices(ballots)

    # remember the candidates we eliminated, their count should be 0
    for candidate in to_eliminate:
        final_result[candidate] = 0
    final_result.update(result)
    return final_result


################################################################################


def count_stv(ballots, num_winners):
    '''
    >>> random.seed(2) # make the random tie-break consistent
    >>> g = ['GREEN', 'NDP', 'BLOC']
    >>> n = ['NDP', 'GREEN', 'BLOC']
    >>> pr_dict(count_stv([g]*5 + [n]*3, 4))
    {'BLOC': 0, 'GREEN': 3, 'NDP': 1}
    '''
    #get the quota
    quota = votes_needed_to_win(ballots, num_winners)

    #convert irv to stv
    irv_to_stv = irv_to_stv_ballot(ballots, num_winners)
    after_transfer = stv_vote_results(irv_to_stv, num_winners)

    #get the dictionary contains all the candidates 
    new_dict=count_approval(ballots)
    for key, value in new_dict.items():
        new_dict[key]=0

    #loop through all the candidates
    for k,v in new_dict.items():
        for key, value in after_transfer.items():
            #compare with the quota and get rid of the last character
            if (value >= quota and key[:-1]==k):
                #update the dictionary
                new_dict[k]=new_dict[k]+1
                
    return new_dict
        
    
    
    


################################################################################


def count_SL(results, num_winners):
    '''
    Return how many seats each party won using the Sainte-Lagu ̈e Method
    >>> A = ['LIBERAL']
    >>> B = ['GREEN']
    >>> C = ['NDP']
    >>> D = ['CPC']
    >>> count_SL([A*10 + B*8 + C*3 + D*2], 8)
    {'LIBERAL': 3, 'GREEN': 3, 'NDP': 1, 'CPC': 1}
    '''
    copy_dict = {}
    seat_dict = {}
    #flatten the input into a list of strings
    results = flatten_lists(results)
    #convert the list to plurality dictionary
    results = count_plurality(results)
    #Copy the results into a new dictionary
    for keys in results:
        copy_dict[keys] = results[keys]
    #create the dictionary for final party-seat pair
    for item in results:
        seat_dict[item] = 0

    count = 0
    #loop until all seats are allocated
    while (count < num_winners):
        #get the first place candidate
        first_place = get_winner(copy_dict)
        #number of seat of that corresponding first place candidate get increased by 1
        seat_dict[first_place] = seat_dict[first_place] + 1
        #update the input using quotient
        copy_dict[first_place] = results[first_place]/(2*seat_dict[first_place]+1)
        count = count +1
    return seat_dict
        
    
    
        
        
    
    


################################################################################


if __name__ == '__main__':
    doctest.testmod()
