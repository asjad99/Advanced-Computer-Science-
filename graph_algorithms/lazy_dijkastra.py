'''

# Shortest Path Algorithm 
return the shortest distance to everynode from the start node s (specified by us)



'''


0 # 0 for directed graph
4 # number of vertices
0 1 4
0 2 1
1 3 1
2 3 5 
3 4 3


input_graph = {
    0: {1: 4, },
    1: {},
    2: {3: 4},
    3: {1: 10},
    4: {2: 15},
}

import math 


def dijkstra(input_graph,n=4,s=0):
	#g - adjacency list of weighted graph 
	#n - numbr of nodes in the graph
	#S - index of the starting node  

	#maintain a 'dist' array where the distance to every node is positive infinity 
	vis = [False,False,False,False]
	dist = [math.inf ,math.inf ,math.inf ,math.inf]
	dist[s] = 0 


	#maintain a PQ of key-valye pairs of (node index, distance) pairs which tell you 
	# which node to visit next based on sorted min value 


	key_value_pairs = {}

	key_value_pairs[0] = 0





