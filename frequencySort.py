class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {}
        for x in s: 
            if x not in d: 
                d[x] = 0
            d[x] += 1
        
        ans = ''
        print (d)
        for x, y in sorted(d.items(), key=lambda x:x[1], reverse = True): 
            ans += x*y
        return ans 

solution = Solution().frequencySort('tree')        
print (solution)
            