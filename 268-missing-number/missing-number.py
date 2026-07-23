class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        
        tsum=n*(n+1)//2
        return tsum-sum(nums)
        