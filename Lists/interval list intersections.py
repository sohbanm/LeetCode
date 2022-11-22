class Solution:
    def intervalIntersection(self, fList: List[List[int]], sList: List[List[int]]) -> List[List[int]]:
        first= second = 0
        res = []
        while first<len(fList) and second<len(sList):
            # print(res)
            if sList[second][1]>=fList[first][1]:
                if sList[second][0]<=fList[first][1]:
                    if sList[second][0]<=fList[first][0]:
                        res.append(fList[first])
                    else:
                        res.append([sList[second][0],fList[first][1]])
                first+=1
            else:
                if fList[first][0]<=sList[second][1]:
                    if fList[first][0]<=sList[second][0]:
                        res.append(sList[second])
                    else:
                        res.append([fList[first][0],sList[second][1]])
                second+=1
            
        return res