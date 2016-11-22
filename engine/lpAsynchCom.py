# -*- coding: utf-8 -*-
#    Copyright (C) 2015
#    All rights reserved.


import networkx as nx
import random

from collections import Counter

def initalize(G):
    """
	This function will initialize the communities label for all the nodes
    """
    # This will try to affect a unique label for each node Cx(0) as discribed in [1]
    # It will have the form {label: node_number}
    labels = {}
    for node in G.nodes():
        labels[node] = node
    return labels

def detectComm(G):
    """
	This function will try to detect a community using the near linear algorithm as 
	discribed in [1].
	
	The implementation was inspired from [1] that were implemented in R but we took our inspiration from [2].

	References
    ----------
    .. [1] Raghavan, Usha Nandini, Réka Albert, and Soundar Kumara. "Near
           linear time algorithm to detect community structures in large-scale
           networks." Physical Review E 76.3 (2007): 036106.
    .. [2] https://networkx.readthedocs.io/en/latest/_modules/networkx/algorithms/community
    """
    labels  = initalize(G)
    check   = True
    b = 0
    while check:
        check = False
        # We need to schuffle the nodes at each iteration of the algorithm (see sect. III (p.4) [1])
        nodes = list(G)
        random.shuffle(nodes)
        freq_label = Counter()
	    # Now we will begin the label propagation for each node :)
        for node in nodes:
            check_label = []
            if len(G.neighbors(node)) == 0:
		        # Here there is no label propagation, cause the node is isolated
		        continue
	    
 	        # Now here, we will try to capture all the labels of the neighbours and
	        # try to see whom is the maximum and then try to change or propagate 
	        # the label throughout the network
	    
            freq_label.clear()
            for neighbour in G[node]:
		        # For each neighboor we mark the it was present by adding
		        # it the the list freq_label and increment their presence
		        # Here the update is asynchronious,   mean each node will
		        # c	 take the t-1 or t th iteration label
		        freq_label.update({labels[neighbour]: 1})
	        
            max_label_freq = max(freq_label.values())
            # The problem here is that maybe we have a lot of common neighboor that have
            # the same label, so we broke tie randomly :)

            bests = [label for label, freq in freq_label.items()
                                        if freq == max_label_freq]
            random.shuffle(bests)
            new_label = random.choice(bests)
            labels[node] = new_label
 	
            # Try to change the exit flag or the stop condition
            check = check or len(bests)>1
        b += 1
    return labels
