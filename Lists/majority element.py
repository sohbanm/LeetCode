class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hash = Counter(nums)
        out=[]
        for num in hash:
            if hash[num]> len(nums)//3:
                out.append(num)
                
        return out