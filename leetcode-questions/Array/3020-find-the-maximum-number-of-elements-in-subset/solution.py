class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}

        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        maxLen = 0

        for x in freq:
            curr = x

            if curr == 1:
                maxLen = max(maxLen, freq[1] if freq[1] % 2 else freq[1] - 1)
                continue

            currLen = 0

            while curr in freq and freq[curr] >= 2:
                currLen += 2
                curr *= curr

            if curr in freq and freq[curr] == 1:
                currLen += 1
            else:
                currLen -= 1

            maxLen = max(maxLen, currLen)

        return maxLen