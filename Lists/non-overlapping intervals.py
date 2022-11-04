class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # intervals.sort(key = lambda i: i[0])
        intervals.sort()
        last = float("-inf")
        res=0
        for l,r in intervals:
            if l<last:
                if r<=last:
                    last = r
                res+=1
                continue
            last = r
        return res