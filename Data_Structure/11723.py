import sys
input = sys.stdin.readline
S = set()
n = int(input())
for _ in range(n):
    command = input().strip().split()

    if len(command) == 2:
        x = int(command[1])
        if command[0] == 'add':
            S.add(x)
        elif command[0] == 'remove':
            S.discard(x)
        elif command[0] == 'check':
            print(1 if x in S else 0)
        elif command[0] == 'toggle':
            if x in S:
                S.remove(x)
            else:
                S.add(x)
    else:
        if command[0] == 'all':
            S = set([i for i in range(1,21)])
        elif command[0] == 'empty':
            S = set()