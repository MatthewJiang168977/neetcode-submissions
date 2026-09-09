class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        def dfs(cur, target, visited):
            print(cur, target)
            if cur == target:
                return True
            visited.add(cur)
            print(visited)
            for neighbor in graph[cur]:
                print(neighbor, "102938109283")
                if neighbor not in visited:
                    print(neighbor, "asdasd")
                    if dfs(neighbor, target, visited):
                        return True
            return False
                    
        for p, q in edges:
            visited = set()
            if p in graph and q in graph and dfs(p, q, visited):
                print(visited)
                return [p, q]
            graph[p].append(q)
            graph[q].append(p)