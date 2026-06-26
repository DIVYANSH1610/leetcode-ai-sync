class Solution(object):
    def assignEdgeWeights(self, edges, queries):
        """
        :type edges: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7

        n = len(edges) + 1

        graph = [[] for _ in range(n + 1)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = 17

        parent = [[0] * (n + 1) for _ in range(LOG)]
        depth = [0] * (n + 1)

        stack = [(1, 0)]

        while stack:
            node, par = stack.pop()

            parent[0][node] = par

            for nei in graph[node]:
                if nei != par:
                    depth[nei] = depth[node] + 1
                    stack.append((nei, node))

        for k in range(1, LOG):
            for v in range(1, n + 1):
                parent[k][v] = parent[k - 1][parent[k - 1][v]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]

            for k in range(LOG):
                if diff & (1 << k):
                    u = parent[k][u]

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]

            return parent[0][u]

        ans = []

        for u, v in queries:
            w = lca(u, v)

            edges_in_path = depth[u] + depth[v] - 2 * depth[w]

            if edges_in_path == 0:
                ans.append(0)
            else:
                ans.append(pow(2, edges_in_path - 1, MOD))

        return ans