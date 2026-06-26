class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count = 0
        n=len(nums)
        for i in range(n):
            target_count=0
            for j in range(i,n):
                if nums[j]==target:
                    target_count+=1
                length = j-i+1
                if target_count>length//2:
                    count+=1
        return count
