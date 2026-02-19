class Solution:
    def dailyTemperatures(self, temp: list[int]) -> list[int]:
        res = [0] * len(temp)
        stack = [] #pair: [temp, index]

        for i, t in enumerate(temp):
            while stack and t > stack[-1][0]:
                stackI = (stack.pop())[1]
                res[stackI] = (i - stackI)
            stack.append([t, i])
        
        return res

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = [temperatures[-1]]
        res = [0]

        for t in reversed(temperatures[:-1]):
            temp = []

            while stack and stack[-1] <= t:
                temp.append(stack.pop())
            
            if len(stack) == 0:
                res.append(0)
            else:
                res.append(len(temp) + 1)
                 
            stack.extend(temp)
            stack.append(t)

            
        return res[::-1]

sol = Solution()
print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))