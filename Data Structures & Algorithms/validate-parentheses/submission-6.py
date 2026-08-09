class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        match = {"]": "[", "}": "{", ")": "("}
        for char in s:
            if char in match:
                if res and res[-1] == match[char]:
                    res.pop()
                else:
                    return False
            else:
                res.append(char)
        if len(res) == 0:
            return True
        return False
