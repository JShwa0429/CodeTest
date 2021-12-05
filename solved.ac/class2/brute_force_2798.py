""" 
카지노에서 제일 인기 있는 게임 블랙잭의 규칙
카드의 합이 21을 넘기지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임

N 장의 카드를 모두 숫자가 보이도록 바닥에 놓는다
딜러는 숫자 M을 크게 외친다

이 때 N장의 카드 중에서 3장을 고른다
플레이어가 고른 카드의 합은 M을 넘지 않으면서
M과 최대한 가깝게 만든다

N 장의 카드에 써져 있는 숫자가 주어졌을 때
M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력하시오
"""
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
cards = list(map(int,input().split()))
max_score = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            total = cards[i] + cards[j] + cards[k]
            if max_score <= total and total <= M:
                max_score = total
print(max_score)