import sys
stack = []
num = int(sys.stdin.readline().strip())
for _ in range(num):
    inputs = sys.stdin.readline().strip()
    if inputs[0] == '1':
        stack.append(inputs.split()[-1])
    elif inputs == '2':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif inputs == '3':
        print(len(stack))
    elif inputs == '4':
        if stack:
            print(0)
        else:
            print(1)
    elif inputs == '5':
        if stack:
            print(stack[-1])
        else:
            print(-1)