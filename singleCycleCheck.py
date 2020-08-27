def hasSingleCycle(array):
	# store indices in HashTable to check if any index is visited twice
	cache = set()
	
	current = 0
	
	# iterate through array
	while len(cache) != len(array):
		print(f"current: {current}")
		
		# return False if index is visited more than once
		if current in cache:
			print("FALSE")
			return False
		
		else:
			cache.add(current)
			
			# calculate next index
			next_ = current + array[current]
			
			if next_ >= 0 and next_ < len(array):
				current = next_
                
			elif next_ < 0:
				
				# calculate how many jumps from end are needed
				kFromEnd = abs(next_) % len(array)
				if kFromEnd == 0:
					current = 0
				else:
					current = len(array) - kFromEnd	
				
			elif next_ >= len(array):
				
				# calculate how many jumps from beginning are needed
				kFromStart = next_ % len(array)
				current = kFromStart
				
	if current != 0:
		return False
			
	return True