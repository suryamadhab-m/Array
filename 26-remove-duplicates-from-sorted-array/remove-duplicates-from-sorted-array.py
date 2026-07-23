class Solution(object):
    def removeDuplicates(self, nums):
        n=len(nums)
        if n==0 or n==1:
            return n
        slow=0

        for fast in range(1, len(nums)):
            if nums[fast]!=nums[slow]:
                slow+=1
                nums[slow]=nums[fast]
        return slow+1    