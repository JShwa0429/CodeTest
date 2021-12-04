N = int(input())
str = []
for i in range(N):
    str.append(input())
str = sorted(list(set(str)))
str = sorted(str,key=lambda s:len(s))

for x in str:
    print(x)

    
