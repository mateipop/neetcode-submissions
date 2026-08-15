class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        negative_index = 0
        result_list = []
        if len(nums) == 3:
            if nums[0] + nums[1] + nums[2] == 0:
                return [nums]
            else:
                return []
        if nums[0] <= 0:
            while negative_index < len(nums) and nums[negative_index] <= 0:
                target = nums[negative_index] * (-1)
                left_index = negative_index + 1
                right_index = len(nums) - 1
                while left_index < right_index:
                    if nums[left_index] + nums[right_index] == target:
                        result_list.append(
                            [nums[negative_index], nums[left_index], nums[right_index]]
                        )
                        left_index, right_index = left_index + 1, right_index - 1

                        while left_index < right_index and nums[left_index] == nums[left_index - 1]:
                            left_index += 1
                        while (
                            left_index < right_index and nums[right_index] == nums[right_index + 1]
                        ):
                            right_index -= 1
                    elif nums[left_index] + nums[right_index] > target:
                        if nums[right_index - 1] == nums[right_index]:
                            while (
                                right_index > left_index
                                and nums[right_index] == nums[right_index - 1]
                            ):
                                right_index -= 1
                        else:
                            right_index -= 1
                    else:
                        if nums[left_index + 1] == nums[left_index]:
                            while (
                                right_index > left_index
                                and nums[left_index] == nums[left_index + 1]
                            ):
                                left_index += 1
                        else:
                            left_index += 1

                while (
                    negative_index <= len(nums) - 2
                    and nums[negative_index] == nums[negative_index + 1]
                ):
                    negative_index += 1
                if negative_index <= len(nums) - 1:
                    negative_index += 1
        else:
            return []
        return result_list
