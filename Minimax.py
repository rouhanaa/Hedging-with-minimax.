from parameters import *
from sys import maxint
import time 
from guppy import hpy

class State(object):
    def __init__(self, var_budg, utility, delta, parent = None,with_child=False):
        self.var_budg = var_budg
        self.utility = utility
        self.delta = delta
        self.parent = parent
        self.with_child= with_child
    def __repr__(self):
        return str([self.var_budg, self.utility, self.delta, self.parent,self.with_child])
    
    def __eq__(self, other):
        return other.var_budg == self.var_budg and other.utility == self.utility
    
    def __cmp__(self, other):
        if self.var_budg != other.var_budg or self.utility != other.utility:
            return -1
        return 0
    
    def __ne__(self, other):
        return self.var_budg != other.var_budg or self.utility != other.utility
    
    def __hash__(self):
        return hash(str(self.var_budg) + str(self.utility))

"""-----------------------------------------------------------INITIALIZATION--------------------------------------------------------------------------------"""
"""
'States' contains a list of sets. Tuples describing each state are then added to the set.
Tuples contain the following information:
    -The variance budget given by c-sum(r[i]^2). (State 1)
    -The utility given by the accumulated sum of -delta*r. (State 2)
    -The associated delta before reaching the state.
    -The parent state.
    -A boolean that indicates whether or not the state admits a child.
""" 

"""-----------------------------------------------------------BUILDING THE STATE MAP --------------------------------------------------------------------------"""        
def build_state_map():
    state_discretization = 0 #If discretization is zero,the difference in utility and variance budget between each state is 0 or 0,1 or 0,01.    
    count_state = 0 #Counts the total number of state.
    states = [set() for d in range(n_trading)]
    #Adding elements to depth 0.
    for r_ in r:
        diff = var_budg - r_ ** 2
        if diff < 0:
            continue
        for d_ in delta:
            states[0].add(State(round(diff, state_discretization),
                                round(initial_utility-d_ * r_, state_discretization),
                                d_))
            count_state += 1
    print "Done with Depth 0..."
    for depth in range(n_trading-1):
        t1=time.time()
        parent_id = -1 #Determines id of the parent state.
        for state in states[depth]:
            state.with_child= False
            break_r_loop = False
            already_present = True
            parent_id+=1
            for d_ in delta:
                """if break_r_loop:
                    break"""
                for r_ in r:
                    diff = state.var_budg - r_ ** 2 
                    if diff < 0: #If the variance budget is negative then the new state will not be created. We skip to the next depth.
                        continue
                    new_state = State(round(diff, state_discretization),
                                      round(state.utility - d_*r_,state_discretization),
                                      d_, 
                                      parent_id,
                                      state.with_child)
                    if new_state not in states[depth+1]:
                        already_present = False
                        states[depth+1].add(new_state)
                        count_state += 1
            if already_present==False:
                state.with_child = True        
        t2=time.time()-t1 # measures time required for each depth
        print "Done with Depth " +str(depth+1)+"..."              
    print "Total number of states: " +str(count_state)
    return states, count_state

"""----------------------------------------------------------MINIMAX ALGORTIHM------------------------------------------------------------------------------- """
def minimax(states):
    print "Minimaxing..."
    depth = n_trading - 1
    while depth > 0:
        print "Depth "+str(depth)+"..."
        states_list = list(states[depth-1]) 
        for parent_id in range(len(states[depth-1])): #considers the potential parent states   
            if states_list[parent_id].with_child==True:
                same_parent_id=get_same_parent( parent_id, states[depth])
                max_set = set()
                if len(same_parent_id)!=0: #groups leafs with the same parent and the same delta 
                    for d_ in delta:
                        same_delta=get_same_delta(d_,same_parent_id)
                        if len(same_delta)!=0:           
                            max_set.add(max(same_delta)) #finds the max. of the list of the leaves with the same delta and adds it to max_set.
                    mn = min(max_set)#finds the min. of max_set  
                    states_list[parent_id]=State(states_list[parent_id].var_budg,
                                                 mn,
                                                 states_list[parent_id].delta,
                                                 states_list[parent_id].parent,
                                                 states_list[parent_id].with_child)
                    #sets mn to be the new utility of the corresponding parent state.
                    if depth - 1 == 0:
                        states_list[parent_id].parent = None
                    states[depth -1] = set(states_list)
        depth -= 1
    max_set_final = set()            
    print "Depth 0..."
    for d_ in delta:
        same_delta = set()
        for s in states[depth]:
            if s.delta == d_:
                same_delta.add(s.utility)
        if len(same_delta)!=0:
            max_set_final.add(max(same_delta))
    return min(max_set_final) 

def get_same_parent(parent_id, depth_set):
        same_parent_id = set()     
        for s in depth_set: #groups leafs with the same parents
            if s.parent == parent_id:
                same_parent_id.add((s.utility, s.delta))  
        return same_parent_id        
def get_same_delta(delta,depth_set):
    same_delta = set() 
    for sp in depth_set:
        if sp[1] == delta:
            same_delta.add(sp[0])
    return same_delta        

t1=time.time()        
states,count = build_state_map()
t2=time.time()
m = minimax(states)

elapsed_minimax=time.time()-t2
h=hpy() #Monitoring memory
print "Value of the optimal strategy is " +str(-m)+" dollars."
print "elapsed time for the minimax:"+str(elapsed_minimax)
print "number of states:"+str(count)
print h.heap()


 

