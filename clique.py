import networkx as nx
import csv
import random
import operator
from collections import defaultdict
import matplotlib.pyplot as plt

def main():
	
	min_clique_size = 8
	percent_of_data = 1.

	data = csv.reader(open('data/newdata.csv'),delimiter=',')
	headers = data.next()
	G = nx.Graph()
	G2 = nx.Graph()
	
	for entry in data:
		if random.random() <= percent_of_data:
		    G.add_edge(int(entry[0]), int(entry[1]))

	cliques = list(nx.find_cliques(G))
	for i in range(len(cliques)):
		cliques[i].sort()

	cliques = sorted(cliques, key=lambda x: len(x))

	popular = defaultdict(int)

	for l in cliques:
		if len(l) >= min_clique_size:
		    print l
		    for person in l:
		    	popular[person] += 1
		    	# uncomment to use clique connections as Graph
		    	#for p2 in l:
		    	#	if person != p2:
		    	#		G2.add_edge(int(person),int(p2))
	
	new_pop = sorted(popular.items(), key=operator.itemgetter(1), reverse=True)
	mostpop = []
	for pop in new_pop[:len(new_pop)/50]:
		print "person %d is in %d cliques" % (pop[0],pop[1])
		mostpop.append(pop[0])

	colorlist = []
	for node in G.nodes():
		if node in mostpop:
			colorlist.append('green')
		else:
			colorlist.append('red')

	nx.draw(G,node_color=colorlist)
	plt.show()
	#nx.draw(G2)
	#plt.show()

if __name__ == '__main__':
	main()
