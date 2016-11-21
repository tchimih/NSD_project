import sys

def saveCom(fout, com, nb, mod):
    """
	This function will only save the output results in an output file
	just in order to debug and analyse the output ... Enjoy :)
    """
    try:

    	file_out = open(fout, "w")
        infos = " # Number of community: " +  str(nb) + "\n" + " # Modularity:" +  str(mod) + "\n"
        file_out.write(infos)
        for node in com:
            line = str(node) + "\t\t" + str(com[node])
            line = line.replace('\n','')
            line += '\n'
            #print line
            file_out.write(line)

        file_out.close()
        return 1
    except:
        print "ERROR: ", sys.exc_info()[0]
        raise
        return 0   
