"""
정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여덟 가지이다.

push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""
from sys import stdin
input = stdin.readline

n = int(input())
deque = []
for i in range(n):
    cmd = input().strip()

    if cmd.startswith('push'):
        push = cmd.split()
        if len(push) != 2:
            print('오류 발생')
            continue
        if push[0] == 'push_front':
            deque.insert(0,push[1])
        elif push[0] == 'push_back':
            deque.append(push[1])

    elif cmd == 'pop_front':
        print(deque.pop(0) if deque else -1)
    elif cmd == 'pop_back':
        print(deque.pop() if deque else -1)

    else:
        if cmd == 'front':
            print(deque[0] if deque else -1)
        elif cmd=='back':
            print(deque[-1] if deque else -1)
        elif cmd=='size':
            print(len(deque) if deque else 0)
        elif cmd=='empty':
            print(0 if deque else 1)
        