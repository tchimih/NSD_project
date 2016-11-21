import argparse
import networkx as nx
import matplotlib.pyplot as plt

from engine.graphFromFile 	import *
from engine.stat			import *
from engine.lpAsynchCom		import *
from engine.test			import *
from engine.save			import *
from engine.modularity		import *
from engine.draw			import *

def main():
    """
	This function will only parse the arguments to get it started :)
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--fileIn" ,help="Name of the file containing the graph", required=True)
    parser.add_argument("-o", "--fileOut",help="Name of the output file", required=True)
    parser.add_argument("-d", "--draw"   ,help="Draw the communities", required=False, type=bool)
    args = parser.parse_args()

    G = graphFromFile(args.fileIn)
    #G=nx.karate_club_graph()
    #getStat(G)
    results = detectComm(G)
    
    modu = modularity(results, G)
    nbCom = len(Counter(results.values()))
    
    print " - Number of community:", nbCom 
    print " - Modularity of commu:", modu

	#drawing
    if (args.draw == True):
        draw(G, results)

    # Now we will need to save the output communities within the specified output file :)
    if saveCom(args.fileOut, results, nbCom, modu):
	print " ********************************************************************* "
	print " \t Communities detected ! "
	print " ********************************************************************* "
    #print list(asyn_lpa_communities(G))
if __name__ == '__main__':
    print " ********************************************************************* "
    print " \t\t\t NSD PROJECT "
    print "  Developped by :\n"
    print "  - HAMMOUTENE ANIS"
    print "  - SAIDI TARIK\n"
    print " ********************************************************************* "
    main()
