class Solution:
    def min_meeting_rooms(self, intervals) -> bool:
        # Write your code here
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        res = 0
        count = 0

        s, e = 0, 0

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
                res = max(res, count)
            else:
                e += 1
                count -= 1

        
        return res
    
sol = Solution()
print(sol.min_meeting_rooms([[0, 30], [5, 10], [15, 20]]))
print(sol.min_meeting_rooms([(2,7)]))


