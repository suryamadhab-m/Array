class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count=0
        cur_count=0
        for n in nums:
            if n==1:
                cur_count+=1
                max_count=max(max_count, cur_count)
            else:
                cur_count=0
        return max_count
        