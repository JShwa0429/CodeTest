""" 
( : )
[ : ]
"""

while True:
    string = input()
    stack = []
    if string == '.':
        break    
    for x in string:
        if x == '(':
            stack.append(x)
        elif x == '[':
            stack.append(x)
        elif x == ')':
            if stack:
                pop = stack.pop()
                if pop != '(':
                    print("no")
                    break
            else:
                print("no")
                break
        elif x == ']':
            if stack:
                pop = stack.pop()
                if pop != '[':
                    print("no")
                    break
            else:
                print("no")
                break
        elif x == '.':
            if not stack:
                print("yes")
            else:
                print("no")
            break

    
