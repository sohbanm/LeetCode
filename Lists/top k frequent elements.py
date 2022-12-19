class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
#less efficient but easier to understand
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        
        for x in nums:
            if x not in count:
                count[x] = 0
            count[x] += 1
            
        output = [] 
        
        for _ in range(k):
            greatest = max(count, key=count.get)
            output.append(greatest)
            count[greatest] = 0
        
        return output