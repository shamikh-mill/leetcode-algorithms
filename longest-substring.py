class Solution(object):
    def lengthOfLongestSubstring(self, s):
    	l = []
    	myMax = 0 
    	res = ""
    	for x in s: 
    		if x not in res:
    			res += x
    		else: 
    			l.append(res)
    			res =  ""	

    	for x in l: 
    		if len(x) > myMax: 
    			myMax = len(x)
    			res = x

    	return res  




if __name__ == '__main__':
	test = Solution()
	print (Solution.lengthOfLongestSubstring(test, "pwwkew")) 