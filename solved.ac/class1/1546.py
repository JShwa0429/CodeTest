import sys

n = int(sys.stdin.readline())
score_list = list(map(int,sys.stdin.readline().split()))
M = max(score_list)
score_list = list(map(lambda score:score / M * 100,score_list))
print(sum(score_list) / len(score_list))

