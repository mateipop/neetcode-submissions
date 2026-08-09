class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(int)
        for i in range(len(nums)):
            if target - nums[i] in seen:
                if seen[target - nums[i]] != i:
                    return [seen[target - nums[i]], i]
            seen[nums[i]] = i
        return False