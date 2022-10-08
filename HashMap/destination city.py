class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        if len(paths) == 1:
            return paths[-1][-1]
        
        map = {}
        for i in range(len(paths)):
            map[paths[i][0]] = paths[i][1]
        
        dest = paths[0][1]
        for i in range(len(paths)):
            if dest in map:
                dest = map[dest]
                
        return dest