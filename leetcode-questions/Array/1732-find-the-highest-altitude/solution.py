class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        n =len(gain)
        mx=0
        for i in range(n+1):
            count = 0
            for j in range(i):
                count+=gain[j]
            mx = max(mx,count)
        return mx
