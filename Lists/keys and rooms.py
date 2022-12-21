import random

class Solution:
    def canVisitAllRooms(rooms):
        if len(rooms[0]) == 0: return False
        keys = set(rooms[0])
        keysX = set([0])
        visited, i = 1, random.sample(keys,1)[0]
        while len(keys)>0:
            for key in rooms[i]:
                if key not in keysX:
                    keys.add(key)
            keys.remove(i)
            keysX.add(i)
            visited+=1
            i=random.sample(keys,1)[0] if len(keys)>0 else i
        if visited==len(rooms): return True
        return False

print(Solution.canVisitAllRooms(rooms = [[1],[2],[3],[]]))