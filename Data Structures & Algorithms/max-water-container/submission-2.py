class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_pointer, right_pointer = 0, len(heights) - 1
        result = 0
        while left_pointer < right_pointer:
            result = max(result, min(heights[left_pointer],heights[right_pointer]) * (right_pointer - left_pointer))
            if heights[left_pointer]<=heights[right_pointer]:
                left_pointer+=1
            else:
                right_pointer-=1

        return result