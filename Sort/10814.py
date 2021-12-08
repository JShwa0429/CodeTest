"""
온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어짐

퀵정렬을 써보자?

"""
import sys
input = sys.stdin.readline

N = int(input())
data = []
for i in range(N):
    age, name = input().split()
    data.append([int(age),name])

data.sort(key=lambda d:(d[0]))

for d in data:
    print(d[0],d[1])







