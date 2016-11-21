import networkx as nx
import re

def graphFromFile(fin):
    """
	This function will allow to convert a text into a nx graph
    """
    # Initialize our graph !
    G = nx.Graph()

    # Try to work with the file
    file_in = open(fin,"rb")
    total_nodes=[]
   
    for text in file_in:
        text = text.replace('\n','')
        tmp = re.split(' ', text)
        if (len(tmp) > 1):
            total_nodes.append(tmp[0])
            total_nodes.append(tmp[1])
	    G.add_edge(tmp[0], tmp[1])
        else:
	    # Presence of an isolated node !
            total_nodes.append(tmp[0])

    #Now we need to construct our graph in a representative way here we :)
    for node in list(set(total_nodes)):
        G.add_node(node)
    
    # Close the graph file, now we don't need it anymore
    file_in.close()
    return G

