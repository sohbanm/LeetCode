# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         if numRows==1:
#             return s
        
#         out = [[] for i in range(numRows)]
#         flag=True
#         i = 0
#         rowIndex = numRows-2
#         while i < len(s):
#             if rowIndex==0:
#                 flag = True
#                 rowIndex = numRows-2
#             if flag:
#                 print(s[i])
#                 for row in range(numRows):
#                     out[row].append(s[i])
#                     if i+1==len(s):
#                         i+=1
#                         break
#                     else:
#                         i+=1

#                 flag = False
#             else:
#                 for row in range(numRows-1,-1,-1):
#                     if row==rowIndex:
#                         out[row].append(s[i])    
#                     else:
#                         out[row].append("")
#                 rowIndex-=1
#                 i+=1
        
#         output = ""
#         for i in range(numRows):
#             output+= "".join(out[i])
#         return output.replace(" ","")


#Thought about the pattern each row has
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1: return s

        res = ""
        for r in range(numRows):
            increment = 2*(numRows-1)
            for i in range(r,len(s),increment):
                res+= s[i]
                if (r>0 and r< numRows-1 and i+increment-2* r < len(s)):
                    res+= s[i+increment-2* r]
                
        return res