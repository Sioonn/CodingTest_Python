N = int(input())
result = -1
for i in range(N):
    if i + sum(map(int,list(str(i)))) == N:
        result = i
        break

if result == -1:
    print(0)
else:
    print(result)