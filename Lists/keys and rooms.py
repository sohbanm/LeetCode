# My own solution O(n)
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if len(rooms[0]) == 0: return False
        keys = set(rooms[0])
        keysX = set([0])
        visited, i = 1, random.choice(tuple(keys))
        while len(keys)>0:
            for key in rooms[i]:
                if key not in keysX:
                    keys.add(key)
            keys.remove(i)
            keysX.add(i)
            visited+=1
            i=random.choice(tuple(keys)) if len(keys)>0 else i
        if visited==len(rooms): return True
        return False

#Breadth First Search Solution O(n)
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def dfs(room):
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    dfs(key)
        
        dfs(0)

        return len(visited) == len(rooms)