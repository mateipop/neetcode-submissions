class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts = defaultdict(int)
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            dicts[s[i]] += 1
            dicts[t[i]] -= 1
        if all(val == 0 for val in dicts.values()):
            return True
        return False