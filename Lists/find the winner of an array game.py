class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        i = 0
        high = 0
        curTotal = 0
        curWin = 0

        while curTotal != k and i < len(arr):
            if arr[0] > arr[1]:
                if arr[0] == curWin:
                    curTotal += 1
                else:
                    high = max(high, arr[0])
                    curWin = arr[0]
                    curTotal = 1
                arr.append(arr.pop(1))
            else:
                if arr[1] == curWin:
                    curTotal += 1
                else:
                    high = max(high, arr[1])
                    curWin = arr[1]
                    curTotal = 1
                arr.append(arr.pop(0))
            i += 1
        
        if curWin != k:
            return high

        return curWin
    