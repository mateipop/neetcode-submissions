class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rezult=[]
        product = 1
        zerocnt = 0
        zerobool = False

        for n in nums:
            if n == 0:
                zerocnt+=1
                zerobool = True
            else:
                product*=n
        
        for n in nums:
            if n == 0:
                if zerocnt>=2:
                    rezult.append(0)
                else:
                    rezult.append(product)
            else:
                if zerocnt:
                    rezult.append(0)
                else:
                    rezult.append(product//n)

        return rezult