class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        p = [-1, -1, -1]

        for i, ch in enumerate(s):
            p[(ord(ch) & 31) - 1] = i
            count += min(p) + 1

        return count
