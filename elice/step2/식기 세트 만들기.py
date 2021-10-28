import sys
C, S, E = map(int,sys.stdin.readline().split());
result = 0

for i in range(0,E):
    chopsticks = C-i
    spoon = S-(E-i)
    
    if chopsticks <= 0 or spoon <= 0:
        continue;

    if chopsticks // 2 <= spoon:
        result = max(result, chopsticks//2)
    else:
        result = max(result, spoon)
print(result)
