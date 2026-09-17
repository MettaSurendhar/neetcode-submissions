from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if not n:
            return True
        
        adj = defaultdict(list)
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        def dfs(node, prev) -> bool:

            if node in visit:
                return False

            visit.add(node)

            for anode in adj[node]:
                if anode == prev:
                    continue
                if not dfs(anode, node) :
                    return False
                
            return True

        return dfs(0,-1) and n==len(visit)

        