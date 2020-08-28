def riverSizes(matrix):
	# initialize cache to store visited indices and an return array
	cache = set()
	riverSizes = []
	
	def getRiverSize(i, j, riverSizes):
		size = 0
		nodesToExplore = [[i, j]]

		while len(nodesToExplore):
			currentNode = nodesToExplore.pop()
			i = currentNode[0]
			j = currentNode[1]
			if (i, j) in cache:
				continue
			cache.add((i, j))
			if matrix[i][j] == 0:
				continue
			size += 1
			unvisitedNeighbors = getUnvisitedNeighbors(i, j)
			for neighbor in unvisitedNeighbors:
				nodesToExplore.append(neighbor)
		if size > 0:
			riverSizes.append(size)
	
	def getUnvisitedNeighbors(i, j):
		unvisitedNeighbors = []
		if i+1 < len(matrix) and (i+1, j) not in cache:
			unvisitedNeighbors.append([i+1, j])
		if i-1 >= 0 and (i-1, j) not in cache:
			unvisitedNeighbors.append([i-1, j])
		if j+1 < len(matrix[0]) and (i, j+1) not in cache:
			unvisitedNeighbors.append([i, j+1])
		if j-1 >= 0 and (i, j-1) not in cache:
			unvisitedNeighbors.append([i, j-1])
		return unvisitedNeighbors
	
	# iterate through each index in matrix
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if (i, j) in cache:
				continue
			getRiverSize(i, j, riverSizes)
	return riverSizes

	