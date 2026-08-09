class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        rez = [0 for i in range(len(temperatures))]
        for index, number in enumerate(temperatures[:-1]):
            cnt = 0
            for i in range(index, len(temperatures)):
                if i == len(temperatures) - 1 and temperatures[i] <= number:
                    cnt = 0
                    break
                if temperatures[i] <= number:
                    cnt += 1
                else:
                    break
            rez[index] = cnt
        return rez