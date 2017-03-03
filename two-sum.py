class Solution(object):
    def twoSum(self, nums, target):
    	l1 = set([])
    	for x in range(len(nums)): 
    		for y in range(1, len(nums)): 
    			if nums[x] + nums[y] == target: 
    				l1.add(x)
    				l1.add(y)

    	return list(l1)

if __name__ == '__main__':
	test = Solution()
	print (Solution.twoSum(test, [3,2,4], 6))