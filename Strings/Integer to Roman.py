class Solution:
    def intToRoman(self, num: int) -> str:
        roman ={1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
        romanIndex = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        out = ''
        index = 12
        while num and index!=-1:
            print(romanIndex[index],num)
            if romanIndex[index]<=num:
                num-=romanIndex[index]
                out+=roman[romanIndex[index]]
            else:
                index-=1
      
        return out
        