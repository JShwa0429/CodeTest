""" 
숫자 카드는 정수 하나가 적혀져 있는 카드이다.
상근이는 숫자 카드 N개를 가지고 있다.
정수 M개가 주어졌을 때,
이 수가 적혀있는 숫자 카드를 상근이는 몇 개 가지고 있는 지 구하시오


조건 1 <= N <= 500,000
숫자카드의 수는 -10,000,000 <= x <= 10,000,000

시간제한 1초
메모리 256MB
"""
import sys
input = sys.stdin.readline
_ = input()
N = map(int,input().split())
_ = input()
M = map(int,input().split())

n_dic = {}
for n in N:
    if n not in n_dic:
        n_dic[n] = 1
    else:
        n_dic[n] +=1

print(' '.join(str(n_dic[x]) if x in n_dic else '0' for x in M))
