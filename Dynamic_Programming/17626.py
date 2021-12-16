n = int(input())
# n보다 작거나 같은 제곱수를 찾고 n-제곱수를 인덱스로 가진 값에 1을 더해주면 된다.
d = [0] * (n + 1)
d[0],d[1] = 0,1

for i in range(2, n+1):
    minValue = 1e9
    j = 1
    while(j**2) <= i:
        minValue = min(minValue,d[i-(j**2)])
        j += 1
    d[i] = minValue + 1
print(d[n])