class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict()
        left_pointer, maxf, res = 0, 0, 0
        res = 0
        for r in range(len(s)):
            count[s[r]] = 1+count.get(s[r],0)
            maxf = max(maxf, count[s[r]])

            while (r-left_pointer+1)-maxf>k:
                    count[s[left_pointer]]-=1
                    left_pointer+=1
            
            res = max(res,r-left_pointer+1)
        
        return res
