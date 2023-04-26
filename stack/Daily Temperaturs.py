class Solution:
    def dailyTemperatures(self, temp: list[int]) -> list[int]:
        res = [0] * len(temp)
        stack = [] #pair: [temp, index]

        for i, t in enumerate(temp):
            while stack and t > stack[-1][0]:
                # stackT, stackI = stack.pop()
                stackI = (stack.pop())[1]
                res[stackI] = (i - stackI)
            stack.append([t, i])
        
        return res

sol = Solution()
print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))