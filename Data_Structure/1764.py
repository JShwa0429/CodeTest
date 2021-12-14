import sys
input = sys.stdin.readline
n, m = map(int,input().split())

listen = [input().strip() for _ in range(n)]
look = [input().strip() for _ in range(n)]

listen_look = sorted(set(listen) & set(look))
print(len(listen_look))
print("\n".join(listen_look))
