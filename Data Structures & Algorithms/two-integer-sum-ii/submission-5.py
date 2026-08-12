class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = defaultdict()
        for index,value in enumerate(numbers):
            if(value in hashmap.keys()):
                return [hashmap[value]+1,index+1]
            hashmap[target-value]=index

        

