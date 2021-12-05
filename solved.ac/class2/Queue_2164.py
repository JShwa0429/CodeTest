""" 
N 장의 카드가 있다.
각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며
1번 카드가 제일 위에, N 번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.

EX ) N = 4
카드는 제일 위에서부터 1234 순서로 놓여있다
1을 버리면 234가 남는다
여기서 2를 제일 아래로 옮기면 342가 된다
3을 버리면 42가 된다
4를 밑으로 옮기면 24가 된다
마지막으로 2를 버리고 나면, 남는 카드가 4가 된다

N이 주어졌을 때 마지막에 남게 되는 카드를 구하는 프로그램 작성
원형큐 구현
front_index : 큐의 첫 부분
rear_index : 큐의 끝 부분

"""
import sys
input = sys.stdin.readline

N = int(input())
Cards = [num+1 for num in range(N)]


front_index = 0
rear_index = N - 1
while front_index != rear_index:  #rear_index와 일치하면 
    Cards[front_index] = 0
    front_index += 1      #pop(0)
    front_index %= N      # 배열 밖으로 나가면 다시 처음으로 보낸다

    rear_index += 1       #맨 뒤 카드 위치
    rear_index %= N       #배열 밖으로 나가면 다시 처음으로 보낸다

    Cards[rear_index] = Cards[front_index]
    Cards[front_index] = 0

    front_index += 1
    front_index %= N      # 배열 밖으로 나가면 다시 처음으로 보낸다
print(Cards[front_index])