class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)
        prefix = 1

        for index in range(0,len(nums)):
            result[index] = prefix
            prefix *= nums[index]

        sufix = 1
        for index in range(len(nums)-1,-1,-1):
            result[index]*=sufix
            sufix*=nums[index]
        return result
