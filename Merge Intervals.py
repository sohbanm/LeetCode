class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals):
            return intervals
        outArr = []

        l, r = 0, 1
        while r < len(intervals):
            left = intervals[l]
            right = intervals[r]
            if left[0] <= right[0]:
                if left[1] <= right[1]:
                    outArr.append([left[0],right[1]])
                else:
                    outArr.append(left)
                    outArr.append(right)
            # else:
            #     if left[1] <= right[1]:
            #         outArr.append([right])
            #     else:
            #         outArr.append([left[0],right[1]])

        return outArr
                    