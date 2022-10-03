class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            temp = digits[i]+1
            if temp==10:
                if i==0:
                    digits.append(0)
                    digits[i] = 1
                else:
                    digits[i] = 0
            else:
                digits[i] = temp
                break
        
        return digits
    
        