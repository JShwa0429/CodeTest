""" 
1 x 1 x 1 로 이루어진 세계 (세로,가로,높이)
세로 : N
가로 : M

위에 블록 제거하여 인벤토리에 넣는 것 : 2초
인벤토리에서 블록 꺼내서 i,j 위에 놓는 것 : 1초

최소시간과 땅의 높이 출력
"""
from collections import Counter
import sys

N, M, B = map(int,sys.stdin.readline().split())
blocks_array = []

for _ in range(N):
    blocks_array.extend(list(map(int, input().split())))
ground = Counter(blocks_array)

res = []
for h in range(max(ground.keys()),-1,-1):
    inventory = B
    needed = 0
    time = 0
    for gh, gc in ground.items():
        if h < gh:
            inventory += (gh - h) * gc
            time += 2 * (gh - h) * gc
        elif h > gh:
            needed += (h - gh) * gc
            time += (h - gh) * gc

    if inventory >= needed:
        res.append([time, h])
res.sort(key=lambda x: (x[0],-x[1]))
print(res[0][0],res[0][1])

# for i in range(N):
#     time = 0
#     for j in range(M):
#         if blocks_array[i][j] > limit:
#             time += (blocks_array[i][j] - limit) * 2
#         elif blocks_array[i][j] < limit:
#             time += limit - blocks_array[i][j]
#     if times > time:
#         times = time
#         time = 0
#     if height < limit:
#         height = limit
#         limit -= 1
# print(times,height)