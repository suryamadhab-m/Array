class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        uniq_cand=len(set(candyType))
        max_all=len(candyType)//2
        min_all=min(max_all, uniq_cand)
        
        return min_all
        