class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # create set to store previously seen values
        cache = set()
        
        # loop through list of integers
        for i in range(len(nums)): # O(n)
            # check if integer is already in cache
            if nums[i] in cache:
                # if it is, return True
                return True
            # else add integer to cache
            cache.add(nums[i])
        # if the end of the loop finishes return False
        return False
        
        