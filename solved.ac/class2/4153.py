while True:
    a,b,c = sorted(list(map(int,input().split())))
    if a <= 0 and b <= 0 and c <= 0:
        break
    
    if pow(a,2) + pow(b,2) == pow(c,2):
        print('right')
    else:
        print('wrong')
