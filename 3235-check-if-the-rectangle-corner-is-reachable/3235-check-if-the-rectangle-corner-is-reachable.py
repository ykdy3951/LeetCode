class Solution:

    LEFT_OR_TOP = 1
    RIGHT_OR_BOTTOM = 2
    INVALID = 3

    def calculate_condition_value(self, x, y, r, xCorner, yCorner) -> int:
        if x * x + y * y <= r * r or (x - xCorner) * (x - xCorner) + (y - yCorner) * (y - yCorner) <= r * r:
            return self.INVALID
        
        ret_val = 0

        if (x <= xCorner and y - r <= 0 and y + r >= 0) or (y <= yCorner and x + r >= xCorner and x - r <= xCorner):
            ret_val += self.RIGHT_OR_BOTTOM
                
        if (y <= yCorner and x - r <= 0 and x + r >= 0) or (x <= xCorner and y + r >= yCorner and y - r <= yCorner):
            ret_val += self.LEFT_OR_TOP
        
        return ret_val

    def dfs(self, now_idx : int, visited : List[bool], is_circle_in_rect : List[bool], condition : List[int], xCorner : int, yCorner : int, circles : List[List[int]]) -> int:
        visited[now_idx] = True
        x, y, r = circles[now_idx]
        condition_val = condition[now_idx]

        for next_idx in range(len(circles)):
            if visited[next_idx]:
                continue

            nx, ny, nr = circles[next_idx]
            dx, dy, dr = x - nx, y - ny, r + nr

            if (dx * dx + dy * dy <= dr * dr and (is_circle_in_rect[now_idx] or is_circle_in_rect[next_idx] or (x + nx <= 2 * xCorner and y + ny <= 2 * yCorner))):
                condition_val |= self.dfs(next_idx, visited, is_circle_in_rect, condition, xCorner, yCorner, circles)
                if condition_val == self.INVALID:
                    return condition_val
        
        return condition_val
            

    def canReachCorner(self, xCorner: int, yCorner: int, circles: List[List[int]]) -> bool:
        condition = [0] * len(circles)
        is_circle_in_rect = [0] * len(circles)

        for idx, circle in enumerate(circles):
            x, y, r = circle
            
            condition[idx] = self.calculate_condition_value(x, y, r, xCorner, yCorner)
            is_circle_in_rect[idx] = (0 <= x <= xCorner and 0 <= y <= yCorner)

            if condition[idx] == self.INVALID:
                return False

        visited = [False] * len(circles)

        for i in range(len(circles)):
            if not visited[i] and self.dfs(i, visited, is_circle_in_rect, condition, xCorner, yCorner, circles) == self.INVALID:
                return False
        
        return True



'''
condition 1 : 원이 원 점이나 모서리에 접할경우 -> return False
condidion 2 : 원이 horizontal or vertical 2개를 포함하는 경우 -> return False
condition 3 : 원이 오른쪽 위 또는 왼쪽 아래를 포함하는 경우 -> return False
'''