class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = defaultdict(int)
        for num in nums:
            seen[num] += 1
        for i in seen:
            if seen[i] > 1:
                return True
        return False