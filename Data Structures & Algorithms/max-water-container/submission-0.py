class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxVolume = 0
        while l < r:
            curVolume = (r - l) * min(heights[l], heights[r])
            if curVolume > maxVolume:
                maxVolume = curVolume
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxVolume
