import sys
n = int(sys.stdin.readline())
A = sorted(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
B = list(map(int,sys.stdin.readline().split()))

for x in B:
    left = 0        # 이분 탐색의 하한치  EX) A[0]
    right = n - 1   # 이분 탐색의 상한치  EX) n = 5 ==> A[4]
    while left <= right:  # 이분 탐색의 하한치가 상한치보다 클 경우 탐색 종료
        middle = (left + right) // 2   # 중간값은 하한치와 상한치의 중간 (소수점 미계산)
        if x > A[middle]:              # 만약 탐색값보다 탐색 자료가 더 클 경우
            left = middle + 1          # 하한치도 탐색값보다 크게 만든다 
        elif x < A[middle]:            # 만약 중간값보다 탐색 자료가 더 작을 경우
            right = middle - 1         # 상한치를 탐색값보다 낮춘다
        elif x == A[middle]:           # 해당 값을 찾았으므로 곧 바로 반복문에서 빠져나온다
            break
    print(1 if x == A[middle] else 0)  # 해당 값을 찾았으면 1, 아니면 0 을 출력