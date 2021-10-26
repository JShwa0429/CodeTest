import sys
N = int(sys.stdin.readline())
for i in range(N):
    R, S = sys.stdin.readline().split()
    print(*map(lambda x: x * int(R), S),sep="")