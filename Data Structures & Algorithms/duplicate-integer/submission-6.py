class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newnums=set(nums)
        if len(newnums) == len(nums):
            return False
        return True