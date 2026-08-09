class Solution:
    def search(self, numbers: List[int], target: int) -> int:
        left = 0
        right = len(numbers)-1
        while left <= right:
            mid = left + int((right-left) / 2)
            if numbers[mid] == target:
                return mid
            elif numbers[mid] > target:
                right = mid-1
            elif numbers[mid] < target:
                left = mid+1
        return -1