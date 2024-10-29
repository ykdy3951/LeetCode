class UF:
    def __init__(self, n : int):
        self.par = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def find(self, node : int) -> int:
        if self.par[node] == node:
            return node

        self.par[node] = self.find(self.par[node])
        return self.par[node]

    def union(self, node1 : int, node2 : int) -> int:
        par1, par2 = self.find(node1), self.find(node2)

        if par1 == par2:
            return 0

        if self.size[par1] > self.size[par2]:
            self.par[par2] = par1
            self.size[par1] += self.size[par2]
            return self.size[par1]
        else:
            self.par[par1] = par2
            self.size[par2] += self.size[par1]
            return self.size[par2]

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        union_find = UF(n * n)
        zero_pos = []

        ans = 1

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    if (i + 1) < n and grid[i + 1][j]:
                        res = union_find.union(i * n + j, (i + 1) * n + j)
                        if res:
                            ans = max(ans, res)
                    if (j + 1) < n and grid[i][j + 1]:
                        res = union_find.union(i * n + j, i * n + j + 1)
                        if res:
                            ans = max(ans, res)
                else:
                    zero_pos.append([i, j])

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for pos in zero_pos:

            graphs = {}

            for i in range(4):
                nx = pos[0] + dx[i]
                ny = pos[1] + dy[i]

                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny]:
                    par = union_find.find(nx * n + ny)
                    graphs[par] = union_find.size[par]

            ans = max(ans, sum(graphs.values()) + 1)

        return ans