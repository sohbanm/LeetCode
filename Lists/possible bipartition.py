# Stupid Question still done understand it
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        d = defaultdict(list)
        for a,b in dislikes:
            d[a].append(b)
            d[b].append(a)
        
        group = {i:None for i in range(1,n+1)}

        def dfs(node,g):
            if not group[node]:
                group[node] = g
            else:
                return group[node] == g
            
            for peeps in d[node]:
                if not dfs(peeps,2 if g==1 else 1):
                    return False
            return True

        for n in range(i,n+1):
            if not group[n] and not dfs(n,1):
                return False
        return True
