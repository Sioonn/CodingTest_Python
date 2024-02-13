import math
N = int(input())
lists = [0]*5001
lists[3],lists[5] = 1,1
result = -1
if (N>5):
    for i in range(6,N+1):
        a = [lists[j] + lists[i-j] for j in range(1, math.ceil(i/2) + 1) if lists[j] != 0 and lists[i-j] != 0]
        if a == []:
            continue
        else:
            lists[i] = min(a)

result = lists[N]

if result == 0:
    print(-1)
else:
    print(result)
