# 지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 
# 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 
# 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.

# 체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 
# 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 
# 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 
# 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

# 보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 
# 당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

N,M = map(int,input().split())
board = []
for i in range(N):
    board.append(input())
repaint = []

for i in range(N-7):
    for j in range(M-7):

        start_white = 0
        start_black = 0

        for k in range(i,i+8):
            for l in range(j,j+8):

                
                # k + l 을 기준으로 홀수 일 때와 짝수일 때를 정한다
                # 기준점은 두 개로 홀수일 때 백일 경우, start_white
                # 흑일 경우, start_black을 기준으로 한다
                if (k + l) % 2 == 0 :
                    # 만약 짝수가 백일 경우, 현재 상태는 백이여야한다
                    # 만약 짝수가 흑일 경우, 현재 상태는 흑이여야한다

                    # 그 기준으로 봤을 때 W이 아니라면, 백을 칠해야하므로 start_white += 1
                    # 흑이 아니라면, 흑을 칠해야하므로 start_black +=1
                    if board[k][l] == 'W':
                        start_black += 1
                    if board[k][l] == 'B':
                        start_white += 1
                else:
                    # 짝수일 때는 그 반대가 되어야한다
                    # 백으로 시작했는데, 짝수도 백이라면 흑을 칠해야한다
                    # 흑으로 시작했는데, 짝수도 흑이라면 백을 칠해야한다

                    if board[k][l] == 'B':
                        start_black += 1
                    if board[k][l] == 'W':
                        start_white += 1

        repaint.append(start_white)
        repaint.append(start_black)

print(min(repaint))