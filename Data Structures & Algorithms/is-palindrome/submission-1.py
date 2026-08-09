class Solution:
    def isPalindrome(self, input: str) -> bool:
        l, r = 0, len(input) - 1
        while l < r:
            while not input[l].isalnum() and l < r:
                l += 1
            while not input[r].isalnum() and r > l:
                r -= 1
            if input[l].lower() != input[r].lower():
                return False
            l, r = l + 1, r - 1
        return True
