""" 
게임 횟수 : X
이긴 게임 : Y (Z%)
Z는 승률, 소수점을 버림
EX) X=53, Y=47 이라면, Z=88

X와 Y가 주어졌을 때, 몇 번 더 게임을 해야 Z가 변하는 지 확인
"""
from sys import stdin
def binary_search(X,Y,Z,start,end):
    if start > end:         # 탐색 종료
        return start       # 탐색 값을 보낸다

    middle = (start+end) // 2
    changed_Z = cal_Z(X + middle, Y + middle)      # 판수가 늘어나서 변동된 승률
    if changed_Z > Z:                              # 승률이 올랐다! 
        return binary_search(X,Y,Z,start,middle-1) # 상한치를 낮춘다!
    else:                                          # 승률이 그대로다!
        return binary_search(X,Y,Z,middle+1,end)   # 하한치를 높인다!

def cal_Z(X,Y):      # 계산용
    return Y*100//X  # Python에는 부동 소수점 오류가 있다
                     # 그래서 부동 소수점을 만들고 X 100 하는 것보다
                     # 100을 먼저 곱하고 Y를 하는 편이 좋다

X, Y = map(int,stdin.readline().split())
Z = cal_Z(X,Y)  
start = 1
end = X * 100

answer = binary_search(X,Y,Z,start,end)
print(answer if answer <= end else -1)


