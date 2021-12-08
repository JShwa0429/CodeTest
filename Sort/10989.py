""" 
N개의 수가 주어졌을 때
이를 오름차순으로 정렬하는 프로그램을 작성하시오
"""
import sys
input = sys.stdin.readline

n = int(input())
nums = {}
for i in range(1,10001):
    nums[i] = 0

for i in range(n):
    num = int(input())
    nums[num] +=1

for key,value in nums.items():
    for _ in range(value):
        print(key)

