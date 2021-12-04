# N = int(input())
# num_list = list(map(int,input().split()))
# sosu = 0

# for num in num_list:
#     error = 0
#     if num > 1 :
#         for i in range(2, num):
#             if num % i == 0:
#                 error += 1
#         if error == 0:
#             sosu += 1
# print(sosu)

# N = int(input())
# num_list = list(map(int,input().split()))
# primes = []

# limit = 1000
# sieve = [False] + [True] * (limit-1)

# m = int(limit ** 0.5)
# for i in range(2,m+1):
#     if sieve[i] == True:
#         for j in range(i*2,limit,i):
#             sieve[j] == False

# cnt = 0
# for x in num_list:
#     if sieve[x-1]:
#         cnt += 1
# print(cnt)

def isPrime(num):
    if num == 1:
        return False
    else:
        for n in range(2, int(num**0.5)+1):
            if num % n == 0:
                return False
        return True

N = int(input())
num_list = list(map(int,input().split()))
cnt = 0

for i in num_list:
    if isPrime(i):
        cnt += 1
print(cnt)
