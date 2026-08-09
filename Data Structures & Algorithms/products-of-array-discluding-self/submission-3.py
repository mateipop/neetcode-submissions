class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1 for x in range(len(nums))]
        temp = 1
        for i in range(len(nums)):
            output[i] = temp
            if i < len(nums) - 1:
                temp *= nums[i]
        temp = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= temp
            if i == 0:
                output[i] = temp
            temp *= nums[i]
        return output