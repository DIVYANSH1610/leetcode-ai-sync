class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        ans = ""

        for i in range(len(words)):
            val = 0

            for j in range(len(words[i])):
                val += weights[ord(words[i][j]) - ord('a')]

            ch = chr(25 - (val % 26) + ord('a'))
            ans += ch

        return ans