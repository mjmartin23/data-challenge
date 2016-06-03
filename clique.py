import networkx as nx
import csv
import random
import operator
from collections import defaultdict
import matplotlib.pyplot as plt

def main():
	
	min_clique_size = 4
	percent_of_data = 1.0

	data = csv.reader(open('data/newdata.csv'))
	headers = data.next()
	G = nx.Graph()	
	
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
	
	new_pop = sorted(popular.items(), key=operator.itemgetter(1), reverse=True)
	for pop in new_pop[:len(new_pop)/10]:
		print "person %d is in %d cliques" % (pop[0],pop[1])

	nx.draw(G)
	plt.show()	    

if __name__ == '__main__':
	main()
