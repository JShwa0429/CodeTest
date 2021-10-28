import sys

n = int(sys.stdin.readline());
for i in range(n):
    ox = list(input())
    score = 0
    continuity = 0
    for x in ox:
        if x == "X":
            continuity = 0
        elif x == "O":
            continuity += 1
        score += continuity
    print(score)