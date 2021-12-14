""" 
몸무게 ,키 : x,y
덩치 : (x,y)
x > p and y > q 라면, 덩치가 더 크다라고 말한다.
그 외에는 같다고 함
"""
import sys
input = sys.stdin.readline


n = int(input())
bulks = []
ranks = []
for _ in range(n):
    bulk = list(map(int,input().split()))
    bulks.append(bulk)

for i in range(len(bulks)):
    rank = 1
    for j in range(len(bulks)):
        if i == j:
            continue
        if bulks[j][0] > bulks[i][0] and bulks[j][1] > bulks[i][1]:
            rank += 1
    ranks.append(rank)

print(" ".join(map(str,ranks)))