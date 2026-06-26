from collections import defaultdict
class Solution(object):
    def getLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 1

        for i in range(n):
            freq = defaultdict(int)
            freq_cnt = defaultdict(int)

            for j in range(i, n):
                x = nums[j]

                old = freq[x]
                if old:
                    freq_cnt[old] -= 1
                    if freq_cnt[old] == 0:
                        del freq_cnt[old]

                freq[x] += 1
                freq_cnt[freq[x]] += 1

                # Only one distinct value
                if len(freq) == 1:
                    ans = max(ans, j - i + 1)
                    continue

                # Must have exactly two frequencies: f and 2f
                if len(freq_cnt) == 2:
                    f1, f2 = freq_cnt.keys()

                    if f1 > f2:
                        f1, f2 = f2, f1

                    if f2 == 2 * f1:
                        ans = max(ans, j - i + 1)

        return ans