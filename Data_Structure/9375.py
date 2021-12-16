t = int(input())
for _ in range(t):
    n = int(input())
    dict = {}
    for _ in range(n):
        clothes, kind = list(input().split())
        if dict.get(kind):
            dict[kind].append(clothes)
        else:
            dict[kind] = [clothes]
    
    result = 1
    for idx, kind in dict.items():
        result *= len(kind) + 1
    print(result - 1)

    


        
