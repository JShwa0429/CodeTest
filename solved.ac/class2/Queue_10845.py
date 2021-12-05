import sys
n = int(sys.stdin.readline())
queue = []
for i in range(n):
    com = sys.stdin.readline()

    if com.startswith('push'):    queue.append(com.split()[1])
    elif com.startswith('front'): print(queue[0] if queue else -1)
    elif com.startswith('back'):  print(queue[-1] if queue else -1)
    elif com.startswith('empty'): print(0 if queue else 1)
    elif com.startswith('size'):  print(len(queue))
    elif com.startswith('pop'):   print(queue.pop(0) if queue else -1)
