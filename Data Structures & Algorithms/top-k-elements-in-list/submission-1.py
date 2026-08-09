class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        storage = defaultdict(int)
        for i in nums:
            storage[i] += 1
        sorted_storage = dict(sorted(storage.items(), key=lambda x: x[1], reverse=True))
        result = []
        for i in sorted_storage:
            result.append(i)
            k -= 1
            if k == 0:
                break
        return result