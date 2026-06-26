
import heapq

class Solution:
    def maxSum(self,nums,k):
        n = len(nums)
        ans = -10**18
        if k == 0 or n == 1:
            sm = 0
            for x in nums:
                sm += x
                ans = max(ans, sm)
                if sm < 0:
                    sm = 0
            return ans

        cnt = 0
        cur_nonneg_sum = 0
        pref = [0] * (n + 1)

        for i in range(n):
            if nums[i] >= 0:
                cur_nonneg_sum += nums[i]
            else:
                cnt += 1
            pref[i + 1] = pref[i] + nums[i]
            ans = max(ans, nums[i])

        if cnt <= k:
            return cur_nonneg_sum

        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            pq = []     
            sm = 0
            for j in range(i, n):
                if nums[j] >= 0:
                    dp[i][j] = sm
                    continue

                if len(pq) < k:
                    heapq.heappush(pq, -nums[j])
                    sm += nums[j]
                else:
                    if -pq[0] > nums[j]:
                        sm -= -pq[0]
                        heapq.heapreplace(pq, -nums[j])
                        sm += nums[j]
     
        for i in range(n):
            pqmax = []   
            sm = 0

            for j in range(i):
                if nums[j] < 0:
                    continue
                if len(pqmax) < k:
                    heapq.heappush(pqmax, nums[j])
                    sm += nums[j]
                else:
                    if pqmax[0] < nums[j]:
                        sm -= pqmax[0]
                        heapq.heapreplace(pqmax, nums[j])
                        sm += nums[j]

            
            for j in range(n - 1, i, -1):
                cur = pref[j + 1] - pref[i]   
                cur -= dp[i][j]               
                cur += sm                     
                ans = max(ans, cur)

                if nums[j] < 0:
                    continue

                if len(pqmax) < k:
                    heapq.heappush(pqmax, nums[j])
                    sm += nums[j]
                else:
                    if pqmax[0] < nums[j]:
                        sm -= pqmax[0]
                        heapq.heapreplace(pqmax, nums[j])
                        sm += nums[j]

                if pqmax:
                    ans = max(ans, sm)

        return ans