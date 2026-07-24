class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n=len(nums)
        cur_window=sum(nums[:k])
        max_window=cur_window
        for i in range(k, n):
            cur_window+=nums[i]-nums[i-k]
            max_window=max(max_window, cur_window)
        return float(max_window)/k