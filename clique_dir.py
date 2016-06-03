import networkx as nx
import csv
import random
import operator
from collections import defaultdict
import matplotlib.pyplot as plt

def main():
    
    min_clique_size = 5
    percent_of_data = .2
    
    fp = open('data/newdata.csv')
    data = csv.reader(fp,delimiter=',')
    headers = data.next()
    G = nx.DiGraph()
    G2 = nx.Graph()
    G3 = nx.Graph()
    
    for entry in data:
        if random.random() <= percent_of_data:
            G.add_edge(int(entry[0]), int(entry[1]))
    # fp.close()
    print "Processed csv file"
    
    # Remove vertices that don't connect to a connected vertex
    for node in G.nodes():
        inedges = list(G.in_edges_iter(node))
        outedges = list(G.out_edges_iter(node))
        # print "Analyzing", node
        # print "Inedges:",inedges
        # print "Out edges:",outedges
        # raw_input('')
        for e in inedges:
            found = False
            for ee in outedges:
                # print "Comparing",e,"and",ee
                # raw_input('')
                if e[0] == ee[1] and ee[0] == e[1]:
                    found = True
                    break
            if not found: 
                G.remove_edge(*e)
                # print "Removed", e
            # else:
            #     print "Kept", e
        # raw_input('')
        
    outdeg = G.out_degree()
    to_remove = [n for n in outdeg if outdeg[n] == 0]
    G.remove_nodes_from(to_remove)
   
    print "Processed graph"
    
    G2 = G.to_undirected()
    
    cliques = list(nx.find_cliques(G2))
    print cliques[-5:]
    for i in range(len(cliques)):
        cliques[i].sort()
    cliques = sorted(cliques, key=lambda x: len(x))
    
    
    # for entry in data:
    #     # Only grab a random sample
    #     if random.random() <= percent_of_data:
    #         G3.add_edge(int(entry[0]), int(entry[1]))
    # cliques = list(nx.find_cliques(G2))
    
    # Popular people -- using a dictionary for fast access
    popular = defaultdict(int)
    for l in cliques:
        if len(l) >= min_clique_size:
            for person in l:
                popular[person] += 1 
                # for p2 in l:
                #     if person != p2:
                #         G3.add_edge(int(person),int(p2))
    
    new_pop = sorted(popular.items(), key=operator.itemgetter(1), reverse=True)
    mostpop = []
    for pop in new_pop[:len(new_pop)/10]:
        print "person %d is in %d cliques" % (pop[0],pop[1])
        mostpop.append(pop[0])

    colorlist = []
    for node in G2.nodes():
        if node in mostpop:
            colorlist.append('green')
        else:
            colorlist.append('red')
    nx.draw(G2,node_color=colorlist)
    plt.show()

if __name__ == '__main__':
    main()
