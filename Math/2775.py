'''
a층의 b호에 살려면, 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다
'''
from sys import stdin
input = stdin.readline
t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input()) 
    apart = [i+1 for i in range(n)]
    for _ in range(k):
        for j in range(1,n):
            apart[j] = apart[j-1] + apart[j]
    print(apart[n-1])
