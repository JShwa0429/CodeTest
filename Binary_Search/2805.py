'''
높이 H >= 0
EX) 20 15 10 17 일 때 H가 15라면 15 15 10 15 가 되며,
    들고가는 나무는 5 + 0 + 0 + 2 = 7
필요한 만큼만 자를 예정이다

나무의 수 N 나무의 길이 M
나무의 높이들 H, 
M <= H.sum() 
M 미터의 나무를 집에 가져가기 위해서, 절단기에 설정할 수 있는 최대 높이를 구하는 프로그램 작성
'''
import sys
input = sys.stdin.readline
n, m = map(int,input().split())
tree_list = list(map(int,input().split()))

def binary_search(start,end,tree_list,m):
    if start > end:                                          # 하한값이 상한값을 초과하면
        return end                                           # 함수 종료 후 상한값(최대값) 리턴
    middle = (start+end)//2                                  # 나무를 자르는 높이

    cut = 0
    for x in tree_list:
        if x > middle:
            cut += (x - middle)                              # 자른 값을 얻는 로직

    if m <= cut:                                             # 만약에 더 잘랐거나 같다면
        return binary_search(middle+1,end,tree_list,m)       # middle 값을 높인다
    else:                                                    # 만약에 덜 잘랐다면
        return binary_search(start,middle-1,tree_list,m)     # middle 값을 낮춘다

start = 1
end = max(tree_list)
print(binary_search(start,end,tree_list,m))


# 반복문을 통해서 해봤는데, 시간초과가 나온다
# start = 1
# end = max(tree_list)
# while start <= end:
#     middle = (start+end)//2
#     cut = 0
#     for tree in tree_list:
#         if tree > middle:
#             cut += tree - middle
#     if m <= cut:
#         start = middle+1
#     else:
#         end = middle-1
# print(end)

