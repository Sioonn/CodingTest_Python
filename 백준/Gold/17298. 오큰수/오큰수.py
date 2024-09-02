import sys
num = int(input())
input_data = list(map(int,sys.stdin.readline().split()))
stack = [0]
result = [-1]*num
for i in range(1,len(input_data)):
    while stack and input_data[stack[-1]] < input_data[i]:
        pop_idx = stack.pop()
        result[pop_idx] = int(input_data[i])
    stack.append(i)

print(*result)