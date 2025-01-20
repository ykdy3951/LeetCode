from heapq import *

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        
        w, h = len(heightMap), len(heightMap[0])
        visited = [[0] * h for _ in range(w)]
        heap = []

        for i in range(w):
            for j in [0, h - 1]:
                heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True

        for j in range(h):
            for i in [0, w - 1]:
                if not visited[i][j]:
                    heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        water = 0

        while heap:
            height, x, y = heappop(heap)
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= w or ny < 0 or ny >= h:
                    continue
                if visited[nx][ny]:
                    continue

                water += max(0, height - heightMap[nx][ny])
                heappush(heap, (max(height, heightMap[nx][ny]), nx, ny))
                visited[nx][ny] = True
        return water