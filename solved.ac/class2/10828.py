"""
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

자료구조 / 스택 문제
"""
import sys


N = int(sys.stdin.readline())
stack = []
for i in range(N):
    try:
        command = sys.stdin.readline().strip().split()
        if command[0] == 'push':
            if len(stack) == 2:
                stack.append(command[1])
        elif command[0] == 'top':
            print(stack[-1] if stack else -1)
        elif command[0] == 'pop':
            pop = -1
            if stack:
                pop = stack[-1]
                stack.pop()
            print(pop)
        elif command[0] == 'size':
            print(len(stack))
        elif command[0] == 'empty':
            print(0 if stack else 1)
    except:
        continue