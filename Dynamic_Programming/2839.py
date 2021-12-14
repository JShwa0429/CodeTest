import sys
input = sys.stdin.readline

N = int(input())
num = []
if N % 5 == 0:
    num.append(N // 5)

for f in range(0,N//5+1):
    for t in range(0,N//3+1):
        if N - (5 * f) - (3*t) == 0:
            num.append(f+t)

print(min(num) if num else -1)
