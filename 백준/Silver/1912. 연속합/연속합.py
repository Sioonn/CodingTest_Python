n = int(input())
sequence = list(map(int,input().split()))

result_list = [sequence[0]] + [0]*(n-1)

temp_add = result_list[0]
for i in range(1,n):
    if temp_add < 0:
        temp_add = 0

    temp_add += sequence[i]
    
    if temp_add >= result_list[i-1]:
        result_list[i] = temp_add
    else:
        result_list[i] = result_list[i-1]


print(result_list[-1])
