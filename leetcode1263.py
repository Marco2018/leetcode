class Solution:
    def minPushBox(self, grid) -> int:
        def bfs_to_reach_S(r, c, x_B, y_B, x_S, y_S):
            curr_level = {(r, c)}
            visited = set()
            while curr_level:
                next_level = set()
                for i, j in curr_level:
                    visited.add((i, j))
                    if i == x_S and j == y_S:
                        return True
                    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        i1, j1 = i + di, j + dj
                        if 0 <= i1 < n and 0 <= j1 < m and (i1, j1) not in visited and (i1, j1) != (x_B, y_B) and \
                                grid[i1][j1] != '#':
                            next_level.add((i1, j1))
                curr_level = next_level
            return False

        def valid_moves(grid, x_B, y_B, x_S, y_S):
            next_moves = []
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                r1, c1 = x_B + dx, y_B + dy
                r2, c2 = x_B - dx, y_B - dy
                if 0 <= r1 < n and 0 <= c1 < m and grid[r1][c1] != '#' and 0 <= r2 < n and 0 <= c2 < m and grid[r2][
                    c2] != '#':
                    if bfs_to_reach_S(r1, c1, x_B, y_B, x_S, y_S):
                        next_moves.append((r2, c2, x_B, y_B))
            return next_moves

        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'B':
                    x_B, y_B = i, j
                elif grid[i][j] == 'S':
                    x_S, y_S = i, j
        grid[x_B][y_B], grid[x_S][y_S] = '.', '.'
        curr_level = {(x_B, y_B, x_S, y_S)}
        visited = set()
        moves = 0
        while curr_level:
            next_level = set()
            for i_B, j_B, i_S, j_S in curr_level:
                visited.add((i_B, j_B, i_S, j_S))
                if grid[i_B][j_B] == 'T':
                    return moves
                for i_B1, j_B1, i_S1, j_S1 in valid_moves(grid, i_B, j_B, i_S, j_S):
                    if (i_B1, j_B1, i_S1, j_S1) not in visited:
                        next_level.add((i_B1, j_B1, i_S1, j_S1))
            curr_level = next_level
            moves += 1
        return -1