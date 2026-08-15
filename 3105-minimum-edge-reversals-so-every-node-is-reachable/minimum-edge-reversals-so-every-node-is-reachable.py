import collections
from typing import List


class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append((v, 0))
            adj[v].append((u, 1))
        ans = [0] * n

        def dfs1(node, parent):
            cost = 0
            for neighbor, weight in adj[node]:
                if neighbor != parent:
                    cost += weight + dfs1(neighbor, node)
            return cost

        ans[0] = dfs1(0, -1)

        def dfs2(node, parent):
            for neighbor, weight in adj[node]:
                if neighbor != parent:
                    if weight == 0:
                        ans[neighbor] = ans[node] + 1
                    else:
                        ans[neighbor] = ans[node] - 1
                    dfs2(neighbor, node)

        dfs2(0, -1)

        return ans
