""" 
이름 궁합
두 사람의 이름을 한 글자씩 번갈아 넣고 획수를 그 아래에 적은 뒤
인접한 숫자끼리 더한 일의 자리 값을 아래에 적어 나가면서 마지막에 남은 두 숫자를 보고
궁합의 정도를 확인

알파벳 획수 = 3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1
"""
import sys
alphabet = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
A = list(map(lambda x: alphabet[ord(x) - 65],sys.stdin.readline().rstrip()))
B = list(map(lambda x: alphabet[ord(x) - 65],sys.stdin.readline().rstrip()))

arr = [[0 for _ in range(len(A) + len(B)) ] for _ in range(len(A)+len(B) - 1)]

for i in range(len(A) + len(B)-1):
    for j in range(i,len(A)+len(B)):
        if i == 0:
            if j % 2 == 0:
                arr[i][j] = A[j//2]
            else:
                arr[i][j] = B[j//2]
            continue
        if j >= i:
            arr[i][j] = (arr[i-1][j-1] + arr[i-1][j]) % 10
print(arr[-1][-2],arr[-1][-1],sep="")

