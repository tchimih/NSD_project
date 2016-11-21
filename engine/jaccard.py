import re
import argparse

from sklearn.metrics import jaccard_similarity_score
from collections import Counter

def infos(fin):
    """
	This function will return the number of communities + the 
	communities .... ENJOY :)
    """
    f = open(fin, "r")
    i = 1
    com = {}
    result = {}

    for line in f:
        if i == 1:
            line = line.replace('\n', '')
            # Get the number of communities !
            n = int(line)
        if i >= 3:
            # Get the communities !
            line = line.replace('\n','')
            tmp = re.split('\t', line)
            com[int(tmp[0])] = int(tmp[1])
        i += 1
    f.close()
    for node in sorted(com.keys()):
        result[node] = com[node]
    return n, result

def normalize(n, c):
    """
	This function will make a concensus on the label chosen
    """
    concensus = {}
    tmp = Counter(c.values())
    keys = sorted(tmp.keys())

    for i in range(0, len(keys)):
	    concensus[i] = keys[i]
  
    for node in c:
	    for v in concensus.keys():
	        if c[node] == concensus.get(v):
			    c[node] = v
    return c
		   
def jaccard_index(fin1, fin2):
    """
		This function will try to compute the similarity between two 
	 	output of community detections .... ENJOY :)
    """
    n1, com1 = infos(fin1)
    n2, com2 = infos(fin2)
	
    #com1 = {12:1, 22:2, 34:1}
    #com2 = {12:26, 22:27, 34:26}
    normalize(n1, com1)
    normalize(n2, com2)
	
    #print com1.values()
    #print com2.values()
    return jaccard_similarity_score(com1.values(), com2.values())


def main():
    """
        This function will only parse the arguments to get it started :)
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-f1", "--fileI" ,help="Name of the file containing the first solution", required=True)
    parser.add_argument("-f2", "--fileII",help="Name of the file containing the second solution", required=True)
    args = parser.parse_args()
    print " Jaccard index = ",jaccard_index(args.fileI, args.fileII)


if __name__ == '__main__':
    print " ********************************************************************* "
    print " \t\t\t JACCARD INDEX COMPUTE "
    print "  Developped by :\n"
    print "  - HAMMOUTENE ANIS"
    print "  - SAIDI TARIK\n"
    print " ********************************************************************* "
    main()

