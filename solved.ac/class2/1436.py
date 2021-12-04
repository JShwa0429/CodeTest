N = int(input())

numbers = []
#초기 값을 While 문 안에 넣는 실수를 하지 말자
i = 666
cnt = 0
while True:
    if '666' in str(i):
        numbers.append(i)
        cnt += 1
    if cnt == N:
        break
    i+=1
print(numbers[N-1])
