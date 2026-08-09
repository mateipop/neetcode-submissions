class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for i in range(len(temperatures))]
        for _, temp in enumerate(temperatures):
            if stack and temp <= stack[-1]:
                stack.append(temp)
            elif not stack:
                stack.append(temp)
            else:
                cnt = 0
                while stack and temp > stack[-1]:
                    cnt += 1
                    if result[_ - cnt] == 0:
                        stack.pop()
                        result[_ - cnt] = cnt
                stack.append(temp)
        return result