import sys

def dfs(x,y): # 깊이 우선 탐색
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]:
            continue
        if ground[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx,ny)

if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 5)
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        m, n, k = map(int,input().split())
        ground = [[0] * m for _ in range(n)]
        visited = [[0] * m for _ in range(n)]
        cnt = 0
        for _ in range(k):
            x, y = map(int,input().split())
            ground[y][x] = 1
        for i in range(n):
            for j in range(m):
                if ground[i][j] and not visited[i][j]:
                    visited[i][j] = 1
                    cnt += 1
                    dfs(i, j)
        print(cnt)