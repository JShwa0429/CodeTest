import sys

n, m = map(int, (sys.stdin.readline()).split())
num = [1]*m

while (m):
    if num[m-1] > n:
        num[m-1] = 1
        num[m-2] += 1
        m -= 1
        continue;
        
    m = len(num)
    print(*num) # num에 담긴 수열을 출력한다
    num[-1] += 1  # 1 1 2   그 뒤 맨 뒤에 숫자를 올린다


# 이중 while문 버전      
# n, m = map(int, input().split())
# num = list(map(lambda x:1,range(m))) # 이러면 [1,1,1] 부터 시작

# while (m):
#     if num[0] > n:  #만약에 수열 앞자리가 n을 초과하면 그대로 종료한다
#         break;
#     print(*num) # num에 담긴 수열을 출력한다
#     num[-1] += 1  # 1 1 2   그 뒤 맨 뒤에 숫자를 올린다
#     if num[-1] > n: # 만약 맨 뒤에 숫자가 수열의 최대값을 초과한다면
#         index = m - 1
#         while(index > 0):
#             if num[index] > n:  # 만약에 입력받은 배열의 해당 index가 최대값을 초과한다면
#                 num[index] = 1  # 현재 위치를 1로 바꾸고
#                 num[index-1] += 1  # 그 앞자리를 1로 추가한다
#             index -= 1


# 재귀 함수 버전
# n, m = map(int, input().split())
# num = list(map(lambda x:1,range(m))) # 이러면 [1,1,1] 부터 시작

# def check(index): # 배열 / 인덱스 / 최대값
#     if index == 0:  # 처음 수라면 그대로 리턴한다
#         return
        
#     if num[index] > n:  # 만약에 입력받은 배열의 해당 index가 최대값을 초과한다면
#         num[index] = 1  # 현재 위치를 1로 바꾸고
#         num[index-1] += 1  # 그 앞자리를 1로 추가한다
#         check(index-1) # 그 다음 그 앞자리를 다시 한번 check한다

# while (m):
#     if num[0] > n:  #만약에 수열 앞자리가 n을 초과하면 그대로 종료한다
#         break;

#     print(*num) # num에 담긴 수열을 출력한다
#     num[-1] += 1  # 1 1 2   그 뒤 맨 뒤에 숫자를 올린다
#     if num[-1] > n: # 만약 맨 뒤에 숫자가 수열의 최대값을 초과한다면
#         check(m-1) # 재귀함수 check를 출력한다
#                    # 빠져나간 뒤에 다시 맨 앞자리가 n을 초과하면 그대로 종료되게 설계되어있다.