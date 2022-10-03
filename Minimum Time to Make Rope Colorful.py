class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        last = ""
        sum = 0
        for i in range(len(colors)):
            if colors[i] == last:
                print(i)
                print(len(colors)//2)
                if i < (len(colors)/2):
                    print(neededTime[i-1])
                    sum+= neededTime[i-1]
                else:
                    print(neededTime[i])
                    sum+= neededTime[i]
            else:
                last = colors[i]
        
        return sum