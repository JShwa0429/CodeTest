import sys
N = int(sys.stdin.readline())
for i in range(N):
    R, S = sys.stdin.readline().split()
    P = map(lambda x: x * int(R), S)
    print(*P,sep="")
