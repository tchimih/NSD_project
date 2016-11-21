import matplotlib.pyplot as plt
import networkx as nx


def draw(G, results):
    """
		This function will simply try to draw the partitions in order to
		give a good idea about the communities .... ENJOY

    """
    size = float(len(set(results.values())))
    pos = nx.spring_layout(G)
    count = 0
    i = 0

    colors = ["red", "green", "blue", "pink", "brown", "yellow", "orange", "#8E24AA", "black", "Cyan", "#76FF03", "#00E676" , "Grey"]

    for com in set(results.values()) :
        list_nodes = [nodes for nodes in results.keys()
                                if results[nodes] == com]
        nx.draw_networkx_nodes(G, pos, list_nodes, node_size = 50,
                                node_color = colors[count])

        count += 1
	nx.draw_networkx_edges(G,pos, alpha=0.2)
    #plt.figure(figsize=(200,100))
    plt.show()

