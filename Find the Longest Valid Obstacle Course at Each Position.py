# tried using memoization
# cannot use first memoized value but the max one
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: list[int]) -> list[int]:
        checked = [0 for _ in range(len(obstacles))]
        res = []

        for i in range(len(obstacles)):
            stuff = obstacles[0:i+1]
            print(stuff)
            length = 0
            temp = float("inf")
            for j in range(len(stuff) - 1, -1, -1):
                print(j)
                print(temp, obstacles[j])
                if temp >= obstacles[j]:
                    if checked[j] != 0:
                        length += checked[j]
                        break
                    length += 1
                    temp = obstacles[j]
            checked[i] = length
            print(checked)
            res.append(length)

        # print(checked)
        return res
    
sol = Solution()
print(sol.longestObstacleCourseAtEachPosition(obstacles = [5,1,5,5,1,3,4,5,1,4]))
# [1,1,2,3,2,3,4,5,3,5]