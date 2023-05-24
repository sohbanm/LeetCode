# tried using memoization
# cannot use first memoized value but the max one, need to use binary search for this
# mahdeen solution
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: list[int]) -> list[int]:
        memo = []
        res = []

        for obstacle in obstacles:
            left, right = 0, len(memo) - 1
            while left <= right:
                mid = (left + right) // 2
                if memo[mid] <= obstacle:
                    left = mid + 1
                else:
                    right = mid - 1
            length = left

            if length == len(memo):
                memo.append(obstacle)
            else:
                memo[length] = obstacle
            res.append(length + 1)

        return res