""" 
2차원 평면 위의 점 N개가 주어진다. 
좌표를 x좌표가 증가하는 순으로, 
x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

#좌표값이 정수하여야한다!!
"""
import sys
n = int(sys.stdin.readline())
dots = []
for i in range(n):
    dots.append(list(map(int,sys.stdin.readline().split())))

dots.sort(key = lambda d:(d[0],d[1]))

for d in dots:
    print(d[0],d[1])

