class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        numsset = set(nums)
        maxlength=0
        for number  in numsset:
            if number-1 not in numsset:
                index=number
                cnt=0
                while index in numsset:
                    cnt+=1
                    index+=1
                
                if cnt>maxlength:
                    maxlength=cnt
        return maxlength
