""" 
이 도시에는 도시를 동쪽과 서쪽으로 나누는 큰 일직선 모양의 강이 있다
다리가 없어서 시민들이 강을 거너는데 큰 불편을 겪고 있다

강 주변에서 다리를 짓기에 적합한 곳을 사이트라고 한다
강의 서쪽에는 N개의 사이트가 있고
동쪽에는 M개의 사이트가 있다 ( N <= M )

최대한 많이 다리를 짓기 위해 N 개만 큼 다리를 지으려고 한다.
다리끼리는 서로 겹칠 수 없다고 할 때, 다리를 지을 수 있는 경우의 수

"""
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int,input().split())
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i == 1:
                dp[i][j] = j
                continue
            if i == j:
                dp[i][j] = 1
            else:
                if j > i:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
    print(dp[n][m])

