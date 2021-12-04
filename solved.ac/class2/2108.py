""" 
수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 
통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.
산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오. 
"""
from collections import Counter
import sys
N = int(sys.stdin.readline())

if N % 2 == 0:
    exit(0)

numbers = []
for i in range(N):
    number = int(sys.stdin.readline())
    numbers.append(number)

numbers.sort()

modes = Counter(numbers).most_common(2)

print(round(sum(numbers)/len(numbers))) #산술평균 . 소수점 이하 첫째 자리에서 반올림
print(numbers[len(numbers)//2]) #중앙값


if len(modes) > 1:
    # 가장 많이 쓴 것끼리 도수가 같으면
    if modes[0][1] == modes[1][1]:
        mode = modes[1][0]
    else:
        mode = modes[0][0]
else:
    mode = modes[0][0]
 #최빈값,여러개가 있을 때는 두 번째로 작은 값
            # 최빈값은 변량 중에서 도수가 가장 큰 값이다.
print(mode)
print(max(numbers) - min(numbers)) #범위 출력


""" 
통계에서
산술평균 : 총합 / 갯수
중앙값 : 가운데 값 - 일단 정렬해야함
최빈값 : 변량 중에서 도수가 가장 큰 값
범위 : 값들이 분포되어있는 방식 [상한값 - 하한값]
"""