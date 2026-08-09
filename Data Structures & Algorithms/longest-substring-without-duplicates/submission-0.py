class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seenSet = set()
        l = 0
        maxLength = 0
        for r in range(len(s)):
            while s[r] in seenSet:
                seenSet.remove(s[l])
                l += 1
            seenSet.add(s[r])
            maxLength = max(maxLength, r - l + 1)
        return maxLength

