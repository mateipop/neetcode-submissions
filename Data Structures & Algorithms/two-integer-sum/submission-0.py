class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_rest = defaultdict(int)
        for i in range(len(nums)):
            seen_rest[nums[i]] = target - nums[i]
            if nums[i] in seen_rest.values():
                index2 = nums.index(seen_rest[nums[i]])
                if(i!=index2):
                    return [index2,i]
        return False