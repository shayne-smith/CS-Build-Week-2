def twoNumberSum(array, targetSum):
    # Write your code here.
	cache = set()
	
	for i, v in enumerate(array):
		diff = targetSum - v
		
		if diff in cache:
			return [diff, v]
		else:
			cache.add(v)
	
	return []
		