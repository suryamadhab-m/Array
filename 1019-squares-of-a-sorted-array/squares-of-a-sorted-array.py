class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sq=[x**2 for x in nums]
        sq.sort()

        return sq