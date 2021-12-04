#이항 계수 구하기 문제
#이항계수란?
#이항식을 이항 정리로 전개했을 때, 각 항의 계수

#(n) ==> nCk = n! / k!(n-k)! 
#(k)
n, k = map(int,input().split())

def factorial(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return num * factorial(num-1)

print(round(factorial(n) / (factorial(k) * factorial(n-k))))
