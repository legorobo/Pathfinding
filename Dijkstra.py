# ------------------------------------------------------------------------
# Dijkstra.py
# ------------------------------------------------------------------------
#
#  Alan Li written on March 17, 2015
# 
#  Waffle Revengeance
#
# ------------------------------------------------------------------------

import sys
import itertools

#AdjacencyGraph
#Dists, Left, Forward, Right, Node Number
n = 'n'
graph = [
		[  21,   1, n, n, 0  ], #Top left starting node
		[ 207,   2, n, n, 1  ],
		[ 284,   3, n, n, 2  ],
		[ 146,  10,12, n, 3  ],
		[ 257,   7, 1, n, 4  ],
		[ 104,   6, n,17, 5  ],
		[ 104,   n, 7, n, 6  ],
		[ 102,   5, 8, n, 7  ],
		[  76,  20, 9, n, 8  ],
		[  56,  11, n, n, 9  ],
		[ 420,   n,11, n, 10 ],
		[ 420,  30, n, n, 11 ],
		[ 117,   n,30, n, 12 ],
		[ 106,  14, n, n, 13 ],
		[  70,  20, n, n, 14 ],
		[ 211,  16, 4, n, 15 ],
		[  47,  24,18, n, 16 ],
		[ 150,   n,24,18, 17 ],
		[  89,   n,19,13, 18 ],
		[  70,  28,21, n, 19 ],
		[ 111,   n,28,21, 20 ],
		[  72,  30, n, n, 21 ],
		[ 104,  19,13, n, 22 ],
		[  47,  15, n, n, 23 ],
		[ 104,  23,32, n, 24 ],
		[  89,   n,23,32, 25 ],
		[  44,   n,22,25, 26 ],
		[  70,  22,25, n, 27 ],
		[ 104,  27,37, n, 28 ],
		[  72,   n,27,37, 29 ],
		[ 305,  29,40, n, 30 ],
		[  47,  45,33, n, 31 ],
		[ 105,   n,45,33, 32 ],
		[  50,  36, n,34, 33 ],
		[ 239,   n,35,26, 34 ],
		[  75,   n,34,36, 35 ],
		[  30,  49,38, n, 36 ],
		[ 105,   n,49,38, 37 ],
		[  72,  40, n, n, 38 ],
		[ 107,   n, n,34, 39 ],
		[ 180,  42,55, n, 40 ],
		[  47,  72, n, n, 41 ],
		[  72,   n, n,49, 42 ],
		[ 158,  44,72, n, 43 ],
		[  47,  58,46, n, 44 ],
		[ 147,   n,58,46, 45 ],
		[  89,   n,48,39, 46 ],
		[  88,  48,39, n, 47 ],
		[  70,  53,50, n, 48 ],
		[ 147,   n,53,50, 49 ],
		[  72,  55, n, n, 50 ],
		[  68,   n,47, n, 51 ],
		[  70,  47, n, n, 52 ],
		[  88,  52,60, n, 53 ],
		[  72,   n,52,60, 54 ],
		[ 162,  54,67, n, 55 ],
		[ 201,  57,43, n, 56 ],
		[  47,  63,59, n, 57 ],
		[ 158,   n,63,59, 58 ],
		[ 161,  65,61, n, 59 ],
		[  68,   n,65,61, 60 ],
		[  72,  67, n, n, 61 ],
		[  47,  56, n, n, 62 ],
		[ 111,  62, n, n, 63 ],
		[ 161,   n,62, n, 64 ],
		[ 111,  64,69, n, 65 ],
		[  72,   n,64,69, 66 ],
		[ 181,  66,71, n, 67 ],
		[ 210,  56, n, n, 68 ],
		[  88,  68, n, n, 69 ],
		[  72,   n,68, n, 70 ],
		[  88,  70, n, n, 71 ],
		[ 147,  31,15, n, 72 ],
		[  21,  71, n, n, 73 ]	#Bottom right starting node
	];

#Regular Dijkstra Algorithm
def dijkstra(start, end):
	checked = [False for x in range(73)];
	dists = [0 for x in range(73)];
	previous = [0 for x in range(73)];
	path = [0 for x in range(73)];

	currentNode = start;
	checked[currentNode] = True;
	while(currentNode != end):
		minDist = sys.maxsize;
		tempDist = 0;
		tempIndex = -1;
		for index,nextNode in enumerate(graph[currentNode][1:3]):
			if(nextNode != "n"):
				tempDist = graph[nextNode][0] + dists[currentNode];
				if(dists[nextNode] == 0):
					if(index == 0):
						path[nextNode] = -90;
					if(index == 1):
						path[nextNode] = 0;
					if(index == 2):
						path[nextNode] = 90;
					previous[nextNode] = currentNode;
					dists[nextNode] = tempDist;
				elif(tempDist < dists[nextNode]):
					if(index == 0):
						path[nextNode] = -90;
					if(index == 1):
						path[nextNode] = 0;
					if(index == 2):
						path[nextNode] = 90;
					dists[nextNode] = tempDist;
					previous[nextNode] = currentNode;
		for index,distance in enumerate(dists):
			if(checked[index] == False and distance > 0 and distance < minDist):
				minDist = distance;
				tempIndex = index;
		currentNode = tempIndex;
		checked[currentNode] = True;
	currentNode = end;
	finalPrevious = [];
	finalPath = ['P'];
	while(currentNode != start):
		finalPrevious.insert(0,previous[currentNode])
		finalPath.insert(0,path[currentNode]);
		currentNode = previous[currentNode]
	return (dists[end],finalPrevious,finalPath);


#Dijkstra algorithm over multiple nodes that need to be moved to
#currentLoc is the current node the robot is on
#nodeHitList is the nodes that the robot needs to go to
def permDijkstra(currentLoc, nodeHitList, exitNode):
	nodePerms = list(itertools.permutations(nodeHitList))	#Generate a list of permutations of the parking lots
	minDist = sys.maxsize;
	tempIndex = -1;
	previous = [];
	dijkstraDist = [0 for x in range(len(nodePerms))];
	dijkstraNode = [0 for x in range(len(nodePerms))];
	dijkstraPath = [0 for x in range(len(nodePerms))];
	for index,i in enumerate(nodePerms):	#Run Dijkstra over all permutations
		for indexJ,j in enumerate(i):
			if(indexJ == 0):
				cDijkstra = dijkstra(currentLoc,i[indexJ])
				dijkstraDist[index] += cDijkstra[0]
				dijkstraNode[index] = cDijkstra[1]
				dijkstraPath[index] = cDijkstra[2]
			else:
				cDijkstra = dijkstra(i[indexJ-1],i[indexJ])
				dijkstraDist[index] += cDijkstra[0]
				dijkstraNode[index].append(cDijkstra[1])
				dijkstraPath[index].append(cDijkstra[2])
		cDijkstra = dijkstra(i[len(nodeHitList)-1],exitNode)
		dijkstraDist[index] += cDijkstra[0]
		dijkstraNode[index].append(cDijkstra[1])
		dijkstraPath[index].append(cDijkstra[2])
		dijkstraPath[index][len(dijkstraPath[index])-1].pop(len(dijkstraPath[index][len(dijkstraPath[index])-1])-1)
		dijkstraPath[index].append("E")
	sys.stdout.write('Permutations: ')
	print(nodePerms)	#Check Permutations
	sys.stdout.write('\nDistances: ')
	print(dijkstraDist)	#Check Distances
	for index,i in enumerate(dijkstraDist):
		if(i < minDist):
			minDist = i
			tempIndex = index;

	sys.stdout.write('\nNode Order: ')
	for i in dijkstraNode[tempIndex]:
		sys.stdout.write(str(i) + " ")
	sys.stdout.write("\n");	#Node Order
	sys.stdout.write('\nInstructions: ')
	for i in dijkstraPath[tempIndex]:
		sys.stdout.write(str(i) + " ")
	sys.stdout.write("\n");	#Drive Commands

	print("\ndist is "+str(dijkstraDist[tempIndex]));

nodeHitList = [20,68,18];	#Put in the 3 parking lots
currentLoc = 0
exitNode = 4
permDijkstra(currentLoc,nodeHitList,exitNode)