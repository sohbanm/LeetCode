class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) -1
        case = len(nums)

        while l <= r:
            m = (l + r) // 2
            print('left:',l,'right:',r)
            print(m)
            if nums[m] > target:
                r = m - 1
                case = m
            elif nums[m] < target:
                l = m + 1
            else:
                print(m)
                return m
        print(case, 'case')
        return case

s1=Solution()
s1.searchInsert(nums = [1,3,5,6], target = 2)